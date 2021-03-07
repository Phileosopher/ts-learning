#include <stdio.h>
 
int main()
{
   int a=100, b=-200, c=500;
   int *p[3];
    
   p[0]= &a;
   p[1]= &b;
   p[2]= &c;
    
   printf("Initial a: %d b: %d c: %d\n",*p[0],*p[1],*p[2]);

   *p[0] += 100;
   *p[1] += 200;
   *p[2] += 300;

   printf("Updated a: %d b: %d c: %d\n",*p[0],*p[1],*p[2]);

   return 0;
}

