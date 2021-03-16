#include <stdio.h>
 
int main()
{
   // int array with 6 elements 
   int arr1[6] = {1,2,3,4,5,6};
   int *ptr1, count=6;

   printf("Initial:  ");
   for(int i=0; i<count; i++)
   {
      printf("%d ",arr1[i]); 
   }
   printf("\n");
    
   for(int i=0; i<count/2; i++)
   {
      ptr1 = &arr1[i]; 
printf("ptr = %d ", *ptr1);

      arr1[i] = arr1[count-i-1]; 
printf("left = %d ", arr1[i]);

      arr1[count-i-1] = *ptr1; 
printf("right = %d\n", *ptr1);
   }

   printf("Reversed: ");
   for(int i=0; i<count; i++)
   {
      printf("%d ",arr1[i]); 
   }
   printf("\n");

   return 0;
}

