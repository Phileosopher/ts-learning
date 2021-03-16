#include <stdio.h>

int main(int argc, char **argv)
{
   int count=1, div=2, num=12;

   while(div < num)
   {
      if(num % div == 0)
      {
         ++count;
      }

      ++div;
   }

   if(count == 1)
   {
      printf("%d is prime\n", num);
   }
   else
   {
      printf("%d is composite\n", num);
   }

   return 0;
}

