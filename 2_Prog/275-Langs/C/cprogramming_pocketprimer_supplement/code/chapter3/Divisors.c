#include <stdio.h>

int main(int argc, char **argv)
{
   int div=2, num=12;

   printf("Number: %d\n", num);

   while(num > 1)
   {
      if(num % div == 0)
      {
         printf("divisor: %d\n", div);
         num /= div;
      }
      else
      {
        ++div;
      }
   }

   return 0;
}

