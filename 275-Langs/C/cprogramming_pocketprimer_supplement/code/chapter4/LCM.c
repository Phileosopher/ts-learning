#include <stdio.h>

int gcd(int num1, int num2)
{
   if(num1 % num2 == 0) 
   {
      return num2;
   }
   else if(num1 < num2) 
   {
    //printf("switching %d and %d\n", num1, num2);
      return gcd(num2, num1);
   }
   else
   {
    //printf("reducing %d and %d\n", num1, num2);
      return gcd(num1-num2, num2);
   }
}

int main(int argc, char **argv)
{
   int gcd1=0, lcm1=0, num1=24, num2=10;
   gcd1 = gcd(num1, num2);
   lcm1 = num1/gcd1*num2/gcd1;

   printf("LCM of %d and %d = %d\n", num1, num2, lcm1);
}

