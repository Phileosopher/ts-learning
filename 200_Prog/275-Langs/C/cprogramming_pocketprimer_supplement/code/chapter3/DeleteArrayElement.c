#include <stdio.h>

int main()
{
   int pos = 4;
   int numbers[] = {15, 3, 99, -4, 25, 8};
   int count=sizeof(numbers)/sizeof(numbers[0]);

   printf("Initial: ");
   for(int i=0; i<count; i++)
   {
      printf("%d ",numbers[i]);
   }
   printf("\n");

   printf("Removed: %d\n",numbers[pos]);
   for(int i=pos-1; i<count-1; i++)
   {
      numbers[i] = numbers[i+1];
   }
   numbers[count-1] = 0;

   printf("Updated: ");
   for(int i=0; i<count; i++)
   {
      printf("%d ",numbers[i]);
   }
   printf("\n");

   return 0;
}

