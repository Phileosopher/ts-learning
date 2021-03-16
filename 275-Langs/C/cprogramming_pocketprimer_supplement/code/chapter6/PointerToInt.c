#include <stdio.h>

int main() 
{
   int x=4;
   int *p = &x;

   printf("x = %d\n", x);
   printf("p = %d\n", *p);
   printf("-------\n");

   *p = 3*x+7;
   printf("p = %d\n", *p);
   printf("x = %d\n", x);
    
   return 0;
}

