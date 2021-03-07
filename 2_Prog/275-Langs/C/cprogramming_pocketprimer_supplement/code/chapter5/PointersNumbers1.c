#include <stdio.h>

int main()
{
   int x=3, y=5;
   int *ptr;

   printf("x = %d\n", x);
   printf("y = %d\n", y);
  
   ptr = &x;
   *ptr = 7;
  
   ptr = &y;
   *ptr = 23;

   printf("x = %d\n", x);
   printf("y = %d\n", y);
  
   return 0;
}

