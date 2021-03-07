#include <stdio.h>

int main() 
{
   int x = 7;
   printf("Value of x:    %d\n", x);

   // ptr “points” to location of x:
   int *ptr = &x;

   // ptr2 points to same location as ptr:
   int *ptr2 = ptr;

   // update value of x:
   *ptr2  = 5678;

   printf("Value of x:    %d\n", x);
   printf("Value of ptr:  %d\n", *ptr2);
   printf("Value of ptr2: %d\n", *ptr2);

   return 0;
}

