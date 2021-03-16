#include <stdio.h>

int gcd(int num1, int num2)
{
   if(num1 % num2 == 0) 
   {
      return num2;
   }
   else if(num1 < num2) 
   {
      printf("switching %d and %d\n", num1, num2);
      return gcd(num2, num1);
   }
   else
   {
      printf("reducing %d and %d\n", num1, num2);
      return gcd(num1-num2, num2);
   }
}

int main(int argc, char **argv)
{
   int result=0, num1=24, num2=10;
   result = gcd(num1, num2);

   printf("GCD of %d and %d = %d\n", num1, num2, result);
}

