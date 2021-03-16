#include <stdio.h>

int fib(int num)
{
   if((num == 0)|| (num == 1))
   {
      return 1;
   }
   else
   {
      return fib(num-1)+fib(num-2);
   }
}

int main(int argc, char **argv)
{
   int result=0, num=10;
   result = fib(num);

   printf("%d fibonacci = %d\n", num, result);
}

