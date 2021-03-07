#include <stdio.h>

int main()
{
   int a1=3, a2=8, a3=6,max=0, min=0;
   max = a1;
   min = a1;

   if( max < a2 ) { max = a2; } 
   if( min > a2 ) { min = a2; } 

   if( max < a3 ) { max = a3; } 
   if( min > a3 ) { min = a3; } 

   printf("ORIGINAL a1: %d a2: %d a3: %d\n", a1, a2, a3);
   printf("MAXIMUM: %d\n", max);
   printf("MINIMUM: %d\n", min);
}

