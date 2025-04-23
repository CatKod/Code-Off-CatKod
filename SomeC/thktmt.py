import re

def analyze_assembly(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    instruction_count = 0
    data_size = 0
    text_size = 0
    format_counts = {'R': 0, 'I': 0, 'J': 0, 'S': 0, 'U': 0, 'B': 0}
    
    data_section = False
    text_section = False
    
    for line in lines:
        line = line.strip()
        
        if line.startswith('.data'):
            data_section = True
            text_section = False
            continue
        elif line.startswith('.text'):
            text_section = True
            data_section = False
            continue
        
        if data_section:
            match = re.search(r'\.asciz\s+"(.*?)"', line)
            if match:
                data_size += len(match.group(1)) + 1  # Thêm 1 byte cho ký tự NULL
        
        if text_section and line and not line.startswith('#'):
            instruction_count += 1
            text_size += 4  # Mỗi lệnh chiếm 4 byte
            
            tokens = line.split()
            if tokens:
                opcode = tokens[0]
                
                if opcode in {'add', 'sub', 'and', 'or', 'sll', 'srl'}:
                    format_counts['R'] += 1
                elif opcode in {'addi', 'andi', 'ori', 'lw', 'li', 'ecall'}:
                    format_counts['I'] += 1
                elif opcode in {'sw'}:
                    format_counts['S'] += 1
                elif opcode in {'beq', 'bge', 'bltz', 'blez'}:
                    format_counts['B'] += 1
                elif opcode in {'j', 'jal'}:
                    format_counts['J'] += 1
                elif opcode in {'lui'}:
                    format_counts['U'] += 1
    
    print(f"Tổng số lượng lệnh máy: {instruction_count}")
    print(f"Dung lượng bộ nhớ dữ liệu (.data): {data_size} bytes")
    print(f"Dung lượng bộ nhớ chương trình (.text): {text_size} bytes")
    print("\nĐếm số lượng lệnh theo 6 khuôn dạng:")
    print(f"- R: {format_counts['R']}")
    print(f"- I: {format_counts['I']}")
    print(f"- J: {format_counts['J']}")
    print(f"- S: {format_counts['S']}")
    print(f"- U: {format_counts['U']}")
    print(f"- B: {format_counts['B']}")

# Chạy phân tích
file_path = '"C:/Users/kimvi/OneDrive - Hanoi University of Science and Technology/Việc tại trường/Kiến trúc máy tính/riscv1.asm"'  # Đổi thành đường dẫn file Assembly của bạn
analyze_assembly(file_path)
