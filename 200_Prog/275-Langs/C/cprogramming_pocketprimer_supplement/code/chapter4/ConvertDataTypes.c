#include <stdlib.h>	
#include <stdio.h>

int main()
{
   int i;
   long l;
   double x;
   char *s;

   s = " -2309.12E-15";
   x = atof(s); /* x = -2309.12E-15 */

   printf("x = %.4e\n",x);


   s = " -9885";
   i = atoi(s);     /* i = -9885 */

   printf("i = %d\n",i);

   s = "98854 dollars";
   l = atol(s);     /* l = 98854 */

   printf("l = %.ld\n",l);

   return (0);
}

