#include <stdio.h>

int main(int argc, char **argv)
{
   int numbers[] = {15, 3, 99, -4, 25, 8};
   int value = 25, pos = -1;

   int count=sizeof(numbers)/sizeof(numbers[0]);

   for(int i=0; i<count; i++)
   {
      if(value == numbers[i])
      {
         pos = i;
         break;
      }
   }

   printf("Array: ");
   for(int i=0; i<count; i++)
   {
      printf("%d ", numbers[i]);
   }
   printf("\n");

   printf("Value: %d\n",value);
   printf("Pos:   %d\n",pos);

   return 0;
}

