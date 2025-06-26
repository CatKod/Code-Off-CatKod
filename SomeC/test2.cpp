#include <stdio.h>
#include <stdbool.h>

int main() {
    typedef struct {
        int year;
        int month; // 1-12
        int day;   // 1-31
        int hour;  // 0-23
        int minute;// 0-59
        int second;// 0-59
    } DateTime;

    // Ví dụ mili giây tương ứng 2025-05-25 20:00:00 UTC
    // Bạn có thể thay đổi time_millis tương ứng test
    long long time_millis = 0x0000019707a7ccc4;
    printf("Time in milliseconds: %lld\n", time_millis);
    long long total_seconds = time_millis / 1000;
    printf("Total seconds: %llx\n", total_seconds);
    // 1970-01-01 00:00:00 UTC
    int year = 1970;

    // Số giây trong 1 ngày
    const int seconds_per_day = 86400;
    const int seconds_per_hour = 3600;
    const int seconds_per_minute = 60;

    // Không dùng hàm con, xử lý trực tiếp
    while (true) {
        int leap = ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0));
        int days_in_year = leap ? 366 : 365;
        long long seconds_in_year = (long long)days_in_year * seconds_per_day;
        if (total_seconds >= seconds_in_year) {
            total_seconds -= seconds_in_year;
            year++;
        } else {
            break;
        }
    }

    int month = 1;
    while (true) {
        int leap = ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0));
        int daysNormal[] = {31,28,31,30,31,30,31,31,30,31,30,31};
        int daysLeap[]   = {31,29,31,30,31,30,31,31,30,31,30,31};
        int dim = leap ? daysLeap[month-1] : daysNormal[month-1];
        long long seconds_in_month = (long long)dim * seconds_per_day;
        if (total_seconds >= seconds_in_month) {
            total_seconds -= seconds_in_month;
            month++;
        } else {
            break;
        }
    }

    // Tính ngày (bắt đầu từ 1)
    int day = (int)(total_seconds / seconds_per_day) + 1;
    total_seconds = total_seconds % seconds_per_day;

    // Tính giờ
    int hour = (int)(total_seconds / seconds_per_hour);
    total_seconds = total_seconds % seconds_per_hour;

    // Tính phút
    int minute = (int)(total_seconds / seconds_per_minute);

    // Tính giây
    int second = (int)(total_seconds % seconds_per_minute);

    DateTime dt;
    dt.year = year;
    dt.month = month;
    dt.day = day;
    dt.hour = hour + 7;
    dt.minute = minute;
    dt.second = second;

    printf("DateTime: %04d-%02d-%02d %02d:%02d:%02d\n",
           dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second);

    return 0;
}