#include <stdio.h>

int main(int argc, char **argv)
{
   int numbers[6] = {15, 3, 99, -4, 25, 8};
   int reverse[6];
   int count=6;

   for(int i=0; i<count; i++)
   {
      reverse[count-1-i] = numbers[i];
   }

   printf("Array:   ");
   for(int i=0; i<count; i++)
   {
      printf("%d ", numbers[i]);
   }
   printf("\n");

   printf("Reverse: ");
   for(int i=0; i<count; i++)
   {
      printf("%d ", reverse[i]);
   }
   printf("\n");

   return 0;
}

