#include <stdio.h>
 
int addAll(int arr[], int size)
{
   int sum=0;

   for(int i=0; i<size; i++)
   {
      sum += arr[i];
   }

   return sum;
}

int main(int argc, char **argv)
{
   // int array with 8 elements 
   int arr1[8] = {1,2,3,4,5,6,7,8};
   int sum=0;

   printf("Values: ");
   for(int i=0; i<8; i++)
   {
      printf("%d ",arr1[i]); 
   }
   printf("\n");

   sum = addAll(arr1,8);
 
   // output the returned value */
   printf("Sum = %d\n", sum);
    
   return 0;
}
