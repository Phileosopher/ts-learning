#include <stdio.h>

int main()
{
   int x=8, y=-12, z=10;

   printf("x: %d y: %d z: %d\n",x,y,z);

   if( x == 3 ) { z = 0; }
   else         { z = 8; }
   printf("x: %d y: %d z: %d\n",x,y,z);
   
   if( y < 0 )  { z *= 3; }
   printf("x: %d y: %d z: %d\n",x,y,z);
   
   if(z % 2 == 0) { x /= 4; }
   else           { y *= -1; }
   printf("x: %d y: %d z: %d\n",x,y,z);
}

