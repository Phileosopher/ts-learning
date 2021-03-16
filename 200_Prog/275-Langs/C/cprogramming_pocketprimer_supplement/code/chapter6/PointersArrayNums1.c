#include <stdio.h>

int main()
{
   int numbers[] = {1,2,3,4,5};
   int *ptr1 = numbers;
   int size1 = sizeof(numbers)/sizeof(int);

   for(int i=0; i<size1; i++)
   {
      printf("%d\n", *(ptr1+i));
   }

   //see what happens when you use these lines:
   //for(int ptr1=numbers; ptr1 != NULL; ptr1++)
   //for(int *ptr1=&numbers[0]; *ptr1 != '\0'; ptr1++)
   //for(int *ptr1=&numbers[0]; *ptr1; ptr1++)

   return 0;
}

