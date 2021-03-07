#include <stdio.h>

int main()
{
   int x=-8, z=10;

   if((z > 5) && (z < 15))
   {
      printf("z between 5 and 15: %d\n", z);
   }
   else 
   {
      printf("z NOT between 5 and 15: %d\n", z);
   }

   if((x < 0) || (z > 4))
   {
      printf("x negative or z greater than 4: %d\n", z);
   }
   else 
   {
      printf("x non-negative or z less than 4: %d\n", z);
   }
}

