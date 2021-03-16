#include <stdio.h>

int main()
{
   int x1=11, x2=4, x3=0;
   double x4;

   x3 = x1/x2;
   x4 = (double) x1/x2;

   printf("x1: %d\n",x1);
   printf("x2: %d\n",x2);
   printf("x3: %d\n",x3);
   printf("x4: %f\n",x4);

   return 0;
}

