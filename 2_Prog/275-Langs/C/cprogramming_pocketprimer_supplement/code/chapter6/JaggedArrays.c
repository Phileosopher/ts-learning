#include <stdio.h>
#include <stdlib.h>

int main()
{
   int rowLengths[] = {6,4,3,5};
   int *ja[4];

   for (int i = 0; i < 4; ++i) 
   {
      ja[i] = (int *)malloc(sizeof(int) * rowLengths[i]);
   }

   for (int i=0; i<4; ++i) 
   {
      for (int j=0; j<rowLengths[i]; ++j) 
      {
         ja[i][j] = i+ j + i*j;
         printf("element (%d,%d) = %d\n", i, j, ja[i][j]);
      }
   }
}

