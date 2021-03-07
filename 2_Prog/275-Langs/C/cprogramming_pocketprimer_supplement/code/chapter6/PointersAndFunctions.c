#include <stdio.h>

void test(int *num) 
{
   *num += 6;
   printf("num inside test: %d\n", *num);
} 

int main()
{
   int num = 7;

   printf("num before test: %d\n", num);
   test(&num);
   printf("num after  test: %d\n", num);
    
   return 0;
} 

