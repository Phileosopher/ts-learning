#include <stdio.h>

void updateMe(int *x)
{
   *x = 3;
   printf("Value of x in updateMe: %d\n", *x);
}

int main() 
{
   int x=7;
   updateMe(&x);
   printf("Value of x in main: %d\n", x);
    
   return 0;
}

