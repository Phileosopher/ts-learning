#include <stdio.h>

void one()
{
   printf("Inside function one\n");
}

void two()
{
   printf("Inside function two\n");
}

int main()
{
   void (*ptr1)();

   one();
   ptr1 = &one;
   (*ptr1)();
   //ptr1 = one;
   //ptr1();

   two();
   ptr1 = &two;
   (*ptr1)();
    
   return 0;
}

