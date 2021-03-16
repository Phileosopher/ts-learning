#include <stdio.h>

int main()
{
   int z=10, y=-123, w=0;

   w = (z/2)*2;
   if(z == w)
   {
      printf("z is even: %d\n", z);
   }
   else 
   {
      printf("z is odd: %d\n", z);
   }

   if(z = y) // do you mean == instead of =?
   {
      printf("z is even: %d\n", z);
   }
   else 
   {
      printf("z is odd: %d\n", z);
   }
}

