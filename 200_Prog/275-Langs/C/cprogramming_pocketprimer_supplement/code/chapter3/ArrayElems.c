#include <stdio.h>

int main ()
{
   int arr1[10]; 

   // initialize element i with value i+100 
   for (int i=0; i<10; i++ )
   {
      arr1[i] = i + 100; 
   }

   for (int j=0; j<10; j++ )
   {
      printf("Element[%d] = %d\n", j, arr1[j] );
   }

   return 0;
}

