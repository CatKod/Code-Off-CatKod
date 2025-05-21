#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX 100

typedef struct {
    char items[MAX][10];
    int top;
} StackStr;

typedef struct {
    int items[MAX];
    int top;
} StackInt;

void pushStr(StackStr* s, char* item) {
    strcpy(s->items[++(s->top)], item);
}

char* popStr(StackStr* s) {
    return s->items[(s->top)--];
}

char* peekStr(StackStr* s) {
    return s->items[s->top];
}

void pushInt(StackInt* s, int item) {
    s->items[++(s->top)] = item;
}

int popInt(StackInt* s) {
    return s->items[(s->top)--];
}

int isOperator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '%';
}

int precedence(char op) {
    if (op == '*' || op == '/' || op == '%') return 2;
    if (op == '+' || op == '-') return 1;
    return 0;
}

void infixToPostfix(char* infix, char postfix[][10], int* postfixLen) {
    StackStr stack;
    stack.top = -1;
    char* token = strtok(infix, " ");
    *postfixLen = 0;

    while (token != NULL) {
        if (isdigit(token[0])) {
            strcpy(postfix[(*postfixLen)++], token);
        } else if (token[0] == '(') {
            pushStr(&stack, token);
        } else if (token[0] == ')') {
            while (stack.top != -1 && peekStr(&stack)[0] != '(') {
                strcpy(postfix[(*postfixLen)++], popStr(&stack));
            }
            popStr(&stack);
        } else if (isOperator(token[0])) {
            while (stack.top != -1 && isOperator(peekStr(&stack)[0]) &&
                   precedence(peekStr(&stack)[0]) >= precedence(token[0])) {
                strcpy(postfix[(*postfixLen)++], popStr(&stack));
            }
            pushStr(&stack, token);
        }
        token = strtok(NULL, " ");
    }

    while (stack.top != -1) {
        strcpy(postfix[(*postfixLen)++], popStr(&stack));
    }
}

int evaluatePostfix(char postfix[][10], int len) {
    StackInt stack;
    stack.top = -1;
    for (int i = 0; i < len; i++) {
        if (isdigit(postfix[i][0])) {
            pushInt(&stack, atoi(postfix[i]));
        } else {
            int b = popInt(&stack);
            int a = popInt(&stack);
            int res;
            switch (postfix[i][0]) {
                case '+': res = a + b; break;
                case '-': res = a - b; break;
                case '*': res = a * b; break;
                case '/': res = a / b; break;
                case '%': res = a % b; break;
            }
            pushInt(&stack, res);
        }
    }
    return popInt(&stack);
}

int main() {
    char infixExpr[200];
    char postfixExpr[MAX][10];
    int postfixLen;

    printf("Nhap bieu thuc trung to (cach nhau boi dau cach): ");
    fgets(infixExpr, sizeof(infixExpr), stdin);
    infixExpr[strcspn(infixExpr, "\n")] = '\0';

    infixToPostfix(infixExpr, postfixExpr, &postfixLen);

    printf("Bieu thuc hau to: ");
    for (int i = 0; i < postfixLen; i++) {
        printf("%s ", postfixExpr[i]);
    }
    printf("\n");

    int result = evaluatePostfix(postfixExpr, postfixLen);
    printf("Gia tri bieu thuc: %d\n", result);

    return 0;
}
