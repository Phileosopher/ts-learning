#include <math.h>
#include <stdio.h>
 
#define PI 3.1415926535

int main()
{
   double pi, x, y1, y2, y3;
 
   x = PI/4;
   y1 = sin(x);
   y2 = cos(x);
   y3 = tan(x);
 
   printf("sin( %lf ) = %lf\n", x, y1);
   printf("cos( %lf ) = %lf\n", x, y2);
   printf("tan( %lf ) = %lf\n", x, y3);

   return(0);
}

