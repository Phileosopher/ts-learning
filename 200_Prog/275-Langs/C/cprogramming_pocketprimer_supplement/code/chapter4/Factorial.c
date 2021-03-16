#include <stdio.h>

int factorial(int num)
{
   if(num > 1)
   {
      return num*factorial(num-1);
   }
   else
   {
      return 1;
   }
}

int main(int argc, char **argv)
{
   int result=0, num=5;
   result = factorial(num);

   printf("%d factorial = %d\n", num, result);
}

