#include <math.h>
#include <stdio.h>

int main()
{
   double y, z;

   y = ceil(1.05);       // y = 2.0
   z = ceil(-1.05);      // z = -1.0
   printf("y = %.2f ; z = %.2f\n", y, z);

   y = floor(2.8);
   z = floor(-2.8);
   printf("y = %.2f ; z = %.2f\n", y, z);

   return 0;
}

