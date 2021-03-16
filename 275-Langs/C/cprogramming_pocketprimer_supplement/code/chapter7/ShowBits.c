#include <stdio.h>
    
void showbits(unsigned int x)
{
   int i; 

   for(i=(sizeof(int)*8)-1; i>=0; i--)
   {
      (x&(1u<<i)) ? putchar('1'): putchar('0');
   }

   printf("\n");
}

int main() 
{
   int j = 5225, m, n;
   printf("%d in binary \t\t ", j);
   showbits(j);

   // the loop for right shift operation 
   for ( m = 0; m <= 5; m++ ) 
   {
      n = j >> m;
      printf("%d right shift %d gives ", j, m);
      showbits(n);
   }

   return 0;
}

