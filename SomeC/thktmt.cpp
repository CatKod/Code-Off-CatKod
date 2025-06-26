#include <stdio.h>

#define MAX 100

int main() {
    char expr[MAX], postfix[MAX][MAX];
    int i = 0, j = 0, k = 0, top = -1;
    char stack[MAX];
    int valStack[MAX], valTop = -1;

    int c;

    printf("Nhap bieu thuc trung to: ");
    while ((c = getchar()) != '\n' && c != EOF) {
        expr[i++] = (char)c;
    }
    expr[i] = '\0';

    i = 0;
    while (expr[i] != '\0') {
        if (expr[i] == ' ') {
            i++;
            continue;
        }

        if (expr[i] >= '0' && expr[i] <= '9') {
            j = 0;
            while (expr[i] >= '0' && expr[i] <= '9') {
                postfix[k][j++] = expr[i++];
            }
            postfix[k][j] = '\0';
            k++;
        } else if (expr[i] == '(') {
            stack[++top] = expr[i++];
        } else if (expr[i] == ')') {
            while (top >= 0 && stack[top] != '(') {
                postfix[k][0] = stack[top--];
                postfix[k][1] = '\0';
                k++;
            }
            if (top >= 0 && stack[top] == '(') top--;
            i++;
        } else {
            char op = expr[i];
            int pri1, pri2;
            if (op == '+' || op == '-') pri1 = 1;
            else if (op == '*' || op == '/' || op == '%') pri1 = 2;
            else pri1 = 0;

            while (top >= 0) {
                if (stack[top] == '(') break;
                if (stack[top] == '+' || stack[top] == '-') pri2 = 1;
                else if (stack[top] == '*' || stack[top] == '/' || stack[top] == '%') pri2 = 2;
                else pri2 = 0;

                if (pri1 <= pri2) {
                    postfix[k][0] = stack[top--];
                    postfix[k][1] = '\0';
                    k++;
                } else break;
            }
            stack[++top] = op;
            i++;
        }
    }

    while (top >= 0) {
        postfix[k][0] = stack[top--];
        postfix[k][1] = '\0';
        k++;
    }

    printf("Bieu thuc hau to: ");
    for (i = 0; i < k; i++) {
        printf("%s ", postfix[i]);
    }
    printf("\n");

    for (i = 0; i < k; i++) {
        if (postfix[i][0] >= '0' && postfix[i][0] <= '9') {
            int num = 0, l = 0;
            while (postfix[i][l] != '\0') {
                num = num * 10 + (postfix[i][l] - '0');
                l++;
            }
            valStack[++valTop] = num;
        } else {
            int b = valStack[valTop--];
            int a = valStack[valTop--];
            int result;
            switch (postfix[i][0]) {
                case '+': result = a + b; break;
                case '-': result = a - b; break;
                case '*': result = a * b; break;
                case '/': result = a / b; break;
                case '%': result = a % b; break;
            }
            valStack[++valTop] = result;
        }
    }

    printf("Gia tri bieu thuc: %d\n", valStack[valTop]);

    return 0;
}
