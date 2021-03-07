#include <stdio.h>

int main()
{
   int number = 0, count=5;
   int *ptr1  = &number;

   for(int i=0; i<count; i++)
   {
      printf("%d\n", *ptr1);
      (*ptr1)++;
   }
    
   return 0;
}

