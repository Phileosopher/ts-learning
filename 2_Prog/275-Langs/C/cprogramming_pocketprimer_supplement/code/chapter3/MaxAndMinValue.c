#include <stdio.h>

int main()
{
   int numbers[] = {15, 3, 99, -4, 25, 8};
   int min=numbers[0], max=numbers[0];
   int count=sizeof(numbers)/sizeof(numbers[0]);

   for(int i=0; i<count; i++)
   {
      if(min > numbers[i])
      {
         min = numbers[i];
      }

      if(max < numbers[i])
      {
         max = numbers[i];
      }
   }

   printf("Array: ");
   for(int i=0; i<count; i++)
   {
      printf("%d ", numbers[i]);
   }
   printf("\n");

   printf("Max:   %d\n",max);
   printf("Min:   %d\n",min);

   return 0;
}

