#include <stdio.h>

int main()
{
   int a1=3, a2=8, a3=6, temp;

   printf("ORIGINAL a1: %d a2: %d a3: %d\n", a1, a2, a3);

   if( a1 < a2 )
   {
      temp = a1;
      a1 = a2;
      a2 = temp;
   } 

   if( a2 < a3 )
   {
      temp = a2;
      a2 = a3;
      a3 = temp;
   }

   printf("ORDERED  a1: %d a2: %d a3: %d\n", a1, a2, a3);
}

