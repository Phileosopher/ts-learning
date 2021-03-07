#include <stdio.h>

int main()
{
   int x1 = 0b11001000;
   int x2 = 0b10111000;
   int x3, x4, x5, x6;
   
   x3 = x1 & x2;
   x4 = x1 | x2;
   x5 = x1 ^ x2;
   x6 = (x1 << 2);

   printf("x1 = %x %d %o\n", x1, x1, x1);
   printf("x2 = %x %d %o\n", x2, x2, x2);
   printf("x3 = %x %d %o\n", x3, x3, x3);
   printf("x4 = %x %d %d\n", x4, x4, x4);
   printf("x5 = %x %d %o\n", x5, x5, x5);
   printf("x6 = %x %d %o\n", x6, x6, x6);
 
   return 0;
}

