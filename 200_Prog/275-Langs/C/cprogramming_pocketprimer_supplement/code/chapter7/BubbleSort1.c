#include <stdio.h>

int main(int argc, char **argv)
{
   int numbers[] = {5, 1, 2, 4, 3};
   int count = sizeof(numbers)/sizeof(numbers[0]);
   int temp;

   printf("Original: ");
   for(int i=0; i<count; i++)
   { 
      printf("%d ",numbers[i]);
   } 
   printf("\n");

   for(int i=0; i<count-1; i++)
   { 
      for(int j=i; j<count; j++)
      { 
         if(numbers[i] > numbers[j])
         {
            temp = numbers[i];
            numbers[i] = numbers[j];
            numbers[j] = temp;
         }
      } 
   } 

   printf("Sorted:   ");
   for(int i=0; i<count; i++)
   { 
      printf("%d ",numbers[i]);
   } 
   printf("\n");
}

