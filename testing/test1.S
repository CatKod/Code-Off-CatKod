.eqv    IN_ADDRESS_HEXA_KEYBOARD   0xFFFF0012  
.eqv    OUT_ADDRESS_HEXA_KEYBOARD  0xFFFF0014
.eqv    TIMER_NOW                  0xFFFF0018 
.eqv    TIMER_CMP                  0xFFFF0020 
.eqv    SEVENSEG_LEFT              0xFFFF0011
.eqv    SEVENSEG_RIGHT             0xFFFF0010
.eqv    SOUND                      0xFFFF0024   # Địa chỉ phát âm thanh (giả định)
.eqv    MASK_CAUSE_TIMER           0x00000004  
.eqv    MASK_CAUSE_KEYPAD          0x00000008  

.data
    digit_patterns: .byte 0x3F, 0x06, 0x5B, 0x4F, 0x66, 0x6D, 0x7D, 0x07, 0x7F, 0x6F
    mode: .word 1      # 1: giờ, 2: phút, 3: giây, 4: ngày, 5: tháng, 6: năm
    time_sec: .word 0  # Số giây hiện tại (cập nhật mỗi giây)
    last_minute: .word -1

.text
.globl main

main:
    # Thiết lập handler ngắt
    la      t0, handler 
    csrrs   zero, utvec, t0 
    li      t1, 0x100 
    csrrs   zero, uie, t1
    csrrsi  zero, uie, 0x10
    csrrsi  zero, ustatus, 1

    # Kích hoạt ngắt bàn phím
    li      t1, IN_ADDRESS_HEXA_KEYBOARD 
    li      t2, 0x80
    sb      t2, 0(t1) 

    # Thiết lập timer ban đầu
    li      t1, TIMER_NOW
    lw      t2, 0(t1)
    li      t3, 1000
    add     t2, t2, t3
    li      t1, TIMER_CMP
    sw      t2, 0(t1)

    # Hiển thị ban đầu
    jal     update_display

loop:
    nop
    j loop

# ----------------- Handler Ngắt -----------------
handler:
    addi    sp, sp, -16
    sw      a0, 0(sp)
    sw      a1, 4(sp)
    sw      a2, 8(sp)
    sw      a7, 12(sp)

    csrr    a1, ucause
    li      a2, 0x7FFFFFFF
    and     a1, a1, a2

    li      a2, MASK_CAUSE_TIMER
    beq     a1, a2, timer_isr
    li      a2, MASK_CAUSE_KEYPAD
    beq     a1, a2, keypad_isr
    j       end_process

timer_isr:
    # Lấy thời gian thực (giả sử TIMER_NOW trả về ms)
    li      t0, TIMER_NOW
    lw      t1, 0(t0)
    div     t1, t1, 1000         # t1 = số giây hiện tại
    sw      t1, time_sec

    # Giải mã thời gian (giờ, phút, giây, ngày, tháng, năm)
    # Giả sử có hàm decode_time (bạn có thể dùng code C chuyển sang asm)
    # Ở đây chỉ demo lấy phút, giây từ t1
    rem     t2, t1, 60           # t2 = giây
    div     t3, t1, 60
    rem     t4, t3, 60           # t4 = phút
    div     t5, t3, 60
    rem     t6, t5, 24           # t6 = giờ

    # Phát âm thanh khi sang phút mới
    lw      t7, last_minute
    bne     t7, t4, play_sound
    j       skip_sound
play_sound:
    li      t8, SOUND
    li      t9, 1
    sw      t9, 0(t8)            # Phát âm thanh
    sw      t4, last_minute
skip_sound:

    # Cập nhật hiển thị
    jal     update_display

    # Đặt lại timer cho lần tiếp theo
    li      t0, TIMER_NOW
    lw      t1, 0(t0)
    li      t2, 1000
    add     t1, t1, t2
    li      t0, TIMER_CMP
    sw      t1, 0(t0)
    j       end_process

keypad_isr:
    # Quét bàn phím, cập nhật mode
    li      t1, IN_ADDRESS_HEXA_KEYBOARD
    li      t2, OUT_ADDRESS_HEXA_KEYBOARD
    li      t3, 0x01
    li      t4, 1
key_row_loop:
    sb      t3, 0(t1)
    lb      a0, 0(t2)
    beq     a0, zero, next_key_row
    # Map phím 1-6 sang mode 1-6
    li      a1, 0x21   # Phím 1
    beq     a0, a1, set_mode1
    li      a1, 0x41   # Phím 2
    beq     a0, a1, set_mode2
    li      a1, 0x81   # Phím 3
    beq     a0, a1, set_mode3
    li      a1, 0x12   # Phím 4
    beq     a0, a1, set_mode4
    li      a1, 0x22   # Phím 5
    beq     a0, a1, set_mode5
    li      a1, 0x42   # Phím 6
    beq     a0, a1, set_mode6
    j       end_keypad
next_key_row:
    slli    t3, t3, 1
    addi    t4, t4, 1
    li      t5, 7
    blt     t4, t5, key_row_loop
    j       end_keypad
set_mode1: li t6, 1; sw t6, mode; j end_keypad
set_mode2: li t6, 2; sw t6, mode; j end_keypad
set_mode3: li t6, 3; sw t6, mode; j end_keypad
set_mode4: li t6, 4; sw t6, mode; j end_keypad
set_mode5: li t6, 5; sw t6, mode; j end_keypad
set_mode6: li t6, 6; sw t6, mode; j end_keypad
end_keypad:
    # Bật lại ngắt keypad
    li      t1, IN_ADDRESS_HEXA_KEYBOARD
    li      t2, 0x80
    sb      t2, 0(t1)
    j       end_process

# ----------------- Hiển thị LED 7 đoạn -----------------
update_display:
    addi    sp, sp, -8
    sw      ra, 0(sp)
    sw      a0, 4(sp)

    lw      t0, mode
    lw      t1, time_sec
    # Giải mã từng mode
    # (Bạn cần thay thế bằng giải mã ngày/tháng/năm thực tế)
    # 1: giờ, 2: phút, 3: giây, 4: ngày, 5: tháng, 6: năm
    div     t2, t1, 60
    div     t3, t2, 60
    rem     t4, t3, 24   # Giờ
    rem     t5, t2, 60   # Phút
    rem     t6, t1, 60   # Giây
    li      t7, 0        # Giá trị hiển thị

    li      t8, 1
    beq     t0, t8, show_hour
    li      t8, 2
    beq     t0, t8, show_minute
    li      t8, 3
    beq     t0, t8, show_second
    # Các mode ngày, tháng, năm bạn cần giải mã thêm từ time_sec
    # Ở đây chỉ demo 3 mode đầu
    j       show_display
show_hour:  mv t7, t4; j show_display
show_minute: mv t7, t5; j show_display
show_second: mv t7, t6; j show_display

show_display:
    # Hiển thị 2 số lên LED 7 đoạn
    li      t8, 10
    rem     t9, t7, t8
    div     t10, t7, t8
    la      t11, digit_patterns
    add     t12, t11, t9
    lb      t13, 0(t12)
    li      t14, SEVENSEG_RIGHT
    sb      t13, 0(t14)
    add     t12, t11, t10
    lb      t13, 0(t12)
    li      t14, SEVENSEG_LEFT
    sb      t13, 0(t14)

    lw      a0, 4(sp)
    lw      ra, 0(sp)
    addi    sp, sp, 8
    ret

end_process:
    lw      a7, 12(sp)
    lw      a2, 8(sp)
    lw      a1, 4(sp)
    lw      a0, 0(sp)
    addi    sp, sp, 16
    uret