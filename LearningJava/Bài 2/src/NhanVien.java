public class NhanVien {
    private String tenNhanVien;
    private double luongCoBan;
    private double heSoLuong;
    private static int soLuongNhanVien = 0;

    public NhanVien(String tenNhanVien, double luongCoBan, double heSoLuong) {
        this.tenNhanVien = tenNhanVien;
        this.luongCoBan = luongCoBan;
        this.heSoLuong = heSoLuong;
        soLuongNhanVien++;
    }

    public boolean tangLuong(double heSoTang) {
        if (heSoTang > 0) {
            this.heSoLuong += heSoTang;
            return true;
        }
        return false;
    }

    public double tinhLuong() {
        return this.luongCoBan * this.heSoLuong;
    }

    public void inTTin() {
        System.out.println("Ten Nhan Vien: " + this.tenNhanVien);
        System.out.println("Luong Co Ban: " + this.luongCoBan);
        System.out.println("He So Luong: " + this.heSoLuong);
        System.out.println("Luong: " + tinhLuong());
    }

    public static int getSoLuongNhanVien() {
        return soLuongNhanVien;
    }

    public static double tinhTongLuong(NhanVien... nhanViens) {
        double tongLuong = 0;
        for (NhanVien nv : nhanViens) {
            tongLuong += nv.tinhLuong();
        }
        return tongLuong;
    }
}