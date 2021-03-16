#include <stdio.h>

int main(int argc, char **argv)
{
   double total=0.0, rowSum=0.0;
   int row=2, col=3; 
   int arr1[2][3]={{1,2,3}, {4,5,6}};

   for(int i=0; i<row; i++)
   {
      rowSum=0.0;
      for(int j=0; j<col; j++)
      {
         total +=  arr1[i][j];
         rowSum += arr1[i][j];
      }

      printf("Sum of row %d: %f\n", i, rowSum);
   }

   printf("Total Sum:     %f\n", total);

   return 0;
}

