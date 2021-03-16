#include <stdio.h>

int main()
{
   int integer1, integer2, sum; 

   printf( "Enter first integer:  " )
   scanf( "%d", &integer1 );

   printf( "Enter second integer: " );
   scanf( "%d", &integer2 );

   sum = integer1 + integer2;
   printf( "Sum is %d\n", sum );
    
   return 0;
}

