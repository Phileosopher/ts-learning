#include <stdio.h>
 
// binary values start with 0b:
int a=0b0101; // decimal value is 5

// octal values start with 0:
int b=016;    // decimal value is 14

// hex values start with 0x or 0X:
int x1=0x18, x2=0X37, x3=0xAB; 

int main() 
{
   int a1=0b0101, b1=0x16, c1=123;
   int x1=0x18, x2=0X37, x3=0xAB; 

   printf("a1=%d b2=%d c3=%d\n",a1, b1, c1);
   printf("x1=%d x2=%d x3=%d\n",x1, x2, x3);

   return 0;
}

