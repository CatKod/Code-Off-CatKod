public class TestNV {
    public static void main(String[] args) {
        NhanVien nv1 = new NhanVien("Hoang Kim Vinh", 15000, 2.5);
        NhanVien nv2 = new NhanVien("Nguyen Tien Dat", 5500, 2.0);
        NhanVien nv3 = new NhanVien("Nguyen Thai Giang", 6000, 2.7);

        nv1.inTTin();
        nv2.inTTin();
        nv3.inTTin();

        nv1.tangLuong(0.5);
        nv2.tangLuong(0.3);
        nv3.tangLuong(0.4);

        System.out.println("Sau khi tang luong:");
        nv1.inTTin();
        nv2.inTTin();
        nv3.inTTin();

        System.out.println("So luong nhan vien hien tai: " + NhanVien.getSoLuongNhanVien());

        //tổng lương
        double tongLuong = NhanVien.tinhTongLuong(nv1, nv2);
        System.out.println("Tong luong cua cac nhan vien: " + tongLuong);

        // So sanh hieu nang giua String and StringBuffer
        int iterations = 100000;

        //String
        long startTimeString = System.currentTimeMillis();
        String str = "";
        for (int i = 0; i < iterations; i++) {
            str += "a";
        }
        long endTimeString = System.currentTimeMillis();
        System.out.println("Time voi String: " + (endTimeString - startTimeString) + " ms");

        //StringBuffer
        long startTimeBuffer = System.currentTimeMillis();
        StringBuffer stringBuffer = new StringBuffer();
        for (int i = 0; i < iterations; i++) {
            stringBuffer.append("a");
        }
        long endTimeBuffer = System.currentTimeMillis();
        System.out.println("Time voi StringBuffer: " + (endTimeBuffer - startTimeBuffer) + " ms");
    }
}