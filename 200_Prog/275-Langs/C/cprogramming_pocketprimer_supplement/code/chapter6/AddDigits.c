#include <stdio.h>
 
int computeSum(int num, int result)
{
    if( num == 0 ) return result;
    computeSum(num/10, result + num % 10);
}

int main()
{
   int number = 123, result = 0;
     
   result = computeSum(number, 0);
   printf("Sum of digits in %d = %d\n", number, result);
    
   return 0;
}

