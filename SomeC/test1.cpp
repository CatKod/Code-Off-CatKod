#include <stdio.h>

int main() {
    int rows;
    printf("Enter the number of rows: ");
    scanf("%d", &rows);

    for (int i = 1; i <= rows - 1; i++) {
        for (int space = 0; space < rows - i; space++)
            printf("   ");

        if (i % 2 == 1) {
            for (int j = 0; j < 2*i; j++) {
                if (j == 0 || j == 2*i - 2)
                    printf(" $ ");
                else
                    printf("   ");
            }
        } else {
            for (int j = 0; j < 2*i; j++) {
                if (j == 0 || j == 2*i - 2)
                    printf(" * ");
                else
                    printf("   ");
            }
        }

        printf("\n");
    }
    if (rows % 2){
        for (int j = 0; j < 2*rows-1; j++) {
            printf(" $ ");
        }
    } else {
        for (int j = 0; j < 2*rows-1; j++) {
            printf(" * ");
        }
    }
    printf("\n");
    return 0;
}
