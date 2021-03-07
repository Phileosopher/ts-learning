#include <stdio.h>

int add(int x, int y)
{
   printf("Inside add\n");
   return (x+y);
}

int multiply(int x, int y, int z)
{
   printf("Inside multiply\n");
   return (x*y*z);
}

int main()
{
   int result, x=3, y=4, z=5;

   int (*ptr1)(int, int);
   int (*ptr2)(int, int, int);

   result = add(x,y);
   printf("Result1:  %d\n", result);

   ptr1 = &add;
   result = (*ptr1)(x,y);
   printf("Result2:  %d\n", result);
   printf("-------------\n");

   result = multiply(x,y,z);
   printf("Result3:  %d\n", result);

   ptr2 = &multiply;
   result = (*ptr2)(x,y,z);
   printf("Result4:  %d\n", result);
    
   return 0;
}

