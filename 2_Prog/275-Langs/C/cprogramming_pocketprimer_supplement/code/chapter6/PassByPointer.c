#include <stdio.h>

int  addNumbers1(int a, int b);
void addNumbers2(int a, int b, int *sum);

int addNumbers1(int a, int b)
{
   return (a+b);
}

void addNumbers2(int a, int b, int *sum)
{
   *sum = a+b;
}

int main()
{
   int num1=3, num2=5, sum1, *sum2=&sum1;

   sum1 = addNumbers1(num1, num2);
   printf("%d + %d = %d\n", num1, num2, sum1);

   addNumbers2(2*num1, 3*num2, sum2);
   printf("%d + %d = %d\n", 2*num1, 3*num2, *sum2);

   return 0;
}

