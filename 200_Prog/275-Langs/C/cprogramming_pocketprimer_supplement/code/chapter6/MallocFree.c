#include <stdio.h>
#include <stdlib.h>
 
int main()
{
   int size=-1, i;
   int* array; 

   do {
      printf("Enter a positive integer: ");
      scanf("%d", &size);
   } while (size <= 0);

   array = (int *)malloc(sizeof(int) * size);
   if (array == NULL) {
      printf("An error creating the dynamic array has occurred.\n");
      return -1;
   }
   
   for (i = 0; i < size; i++) {
      array[i] = 1;
      printf("array[%d] has been assigned value 1.\n", i);
   }

   free(array); 

   return 0;
}

