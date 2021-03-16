#include <stdio.h>

int main() 
{
   int x = 7;
   printf("Value of x: %d\n", x);

   int *ptr = &x;
   *ptr = 45;
   printf("Value of x: %d\n", x);

   *(&x) = 1234;
   printf("Value of x: %d\n", x);

   int *ptr2 = ptr;
   *ptr2  = 5678;
   printf("Value of x: %d\n", x);

   return 0;
}

