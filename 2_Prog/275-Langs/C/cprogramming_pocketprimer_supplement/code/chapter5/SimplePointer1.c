#include <stdio.h>

int main() 
{
   int x = 7;
   printf("Value of x:    %d\n", x);

   // ptr “points” to location of x:
   int *ptr = &x;
   *ptr = 45;
   printf("Value of x:    %d\n", x);

   // update value of x to 1234;
   *(&x) = 1234;
   printf("Value of x:    %d\n", x);

   // error:
   // error: cannot assign x to an explicit address
 //&x = 1234;

   return 0;
}

