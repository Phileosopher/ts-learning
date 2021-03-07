#include <stdio.h>

int array[] = {4, 5, 8, 9, 8, 1, 0, 1, 9, 3}; 

int main()
{
   int index;
   while (array[index] != 0)

   ++index;
   printf("Number of elements before 9: %d\n", index);

   return (0);
}

