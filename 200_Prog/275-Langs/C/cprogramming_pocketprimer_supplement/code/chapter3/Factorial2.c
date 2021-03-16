#include <stdio.h>

int main()
{
   int result=1, num=5;

   for(int i=1; i<=num; i++)
   {
      result *= i;
   }

   printf("%d factorial = %d\n", num, result);

   return 0;
}

