#include <stdio.h>

int countDigits(int num, int result)
{
    if( num == 0 ) return result;
    countDigits(num/10, result+1);
}

int main()
{
   int number = 123, result = 0;

   result = countDigits(number, 0);
   printf("Number of digits in %d = %d\n", number, result);

   return 0;
}

