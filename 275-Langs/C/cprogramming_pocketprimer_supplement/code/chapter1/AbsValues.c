#include <math.h>
#include <stdlib.h>
#include <stdio.h>
 
int main(int argc, char **argv)
{
   int x1 = -4, y1;
   double x2=-11.23,y2;

   y1 = abs(x1);
   printf("The absolute value of x1 is %d\n", y1);

   y2 = fabs(x2);
   printf("fabs( %lf ) = %lf\n", x2, y2);
}

