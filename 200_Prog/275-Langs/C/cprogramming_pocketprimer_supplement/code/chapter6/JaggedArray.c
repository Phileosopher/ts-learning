#include <stdio.h>
#include <stdlib.h>

int main()
{
   int *const jagged1[] = { 
     (int []) { 0, 1 }, 
     (int []) { 1, 2, 3 } 
   };

   int jagged2[][3] = { {10,12}, {21,32,45} };

   int size1 = sizeof(jagged1);
   int size2 = sizeof(jagged2);
   printf("size1 = %d\n", size1);
   printf("size2 = %d\n", size2);

/*
   int* ptr1 = (void*)jagged1;
   for (int i=0;i<(size1/(int)sizeof(int));i++)
   {
      printf("%d = %d\n", i, *ptr1++);
   }
*/

   int* ptr2 = (void*)jagged2;
   for (int i=0;i<(size2/(int)sizeof(int));i++)
   {
      printf("%d = %d\n", i, *ptr2++);
   }

/*
   int jagged[5][10];
   int jaggedLengths[] = {10, 5, 4, 1, 3};
   int i, j;
   
   for (i = 0; i < 5; ++i) 
   {
      jagged[i] = (int [])malloc(sizeof(int) * jaggedLengths[i]);
      for (j = 0; j < jaggedLengths[i]; ++j)
      {
         jagged[i][j] = i+j;
      }
   }
   
   // display the data
   for (i=0; i<5; ++i)
   {
      for (j = 0; j < jaggedLengths[i]; ++j)
      {
         printf("%d\n", jagged[i][j]);
      }
   }
*/
}

