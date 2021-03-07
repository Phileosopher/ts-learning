#include <stdio.h>

void ptrArray(int *arr, int row, int col)
{
   for(int i=0; i<row; i++)
   {
      printf("Row %d: ",i);
      for(int j=0; j<col; j++)
      {
         printf("%d ", *(arr+i*row+j));
      }
      printf("\n");
   }
}

int main()
{
   int row=3, col=3, temp=0;
   int arr1[3][3]={{1,2,3}, 
                   {4,5,6},
                   {7,8,9}};

   // display original matrix 
   printf("Original\n");
   ptrArray(&arr1[0][0], row, col);

   for(int i=1; i<row; i++)
   {
      for(int j=0; j<i; j++)
      {
         temp = arr1[i][j];
         arr1[i][j] = arr1[j][i];
         arr1[j][i] = temp;
      }
   }

   // display transposed matrix 
   printf("Transpose\n");
   ptrArray(&arr1[0][0], col, row);
  
   return 0;
}

