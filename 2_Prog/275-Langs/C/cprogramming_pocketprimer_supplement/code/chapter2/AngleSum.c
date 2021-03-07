#include <stdio.h>

int main()
{
   int a1=40, a2=80, a3=0;
   // ensure the following are true:
   // 1) a1>0 and a1 < 180
   // 2) a2>0 and a2 < 180
   // 3) a1+a1 < 180

   if( ((a1 <= 0) || (a1 >= 180))  || 
       ((a2 <= 0) || (a2 >= 180)) ) 
   {
      printf("angles out of range: a1 = %d a2 = %d\n", a1, a2);
   }
   else 
   {
      if( a1+a2 >= 180) 
      {
         printf("a1 + a2 is too large: %d\n", a1+a2);
      }
      else 
      {
         a3 = 180 - (a1+a2);
         printf("a1: %d a2: %d a3: %d\n", a1, a2, a3);
      }
   }
}

