#include <stdio.h>

#define add2(num1, num2) { \
    int total=0;           \
    sum = num1 + num2;     \
}

int main()
{
    int sum, num1=5, num2=8;
    add2(num1, num2);
    printf("num1 = %i num2 = %i sum = %i\n", num1, num2, sum);
    return 0;
}
