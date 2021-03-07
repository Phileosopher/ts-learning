#include <stdio.h>

void squaredValues(int startValue, int endValue, int (*fp) (int)) 
{
   printf("Calculating Squared Values\n");
   printf("--------------------------\n");
   for(int x=startValue; x<endValue; x++)
   {
      printf("%2d   %3d\n", x, (*fp)(x));
   }
   printf("\n");
}

int square(int x) {
   return x*x;
}

void cubedValues(int startValue, int endValue, int (*fp) (int)) 
{
   printf("Calculating Cubed Values\n");
   printf("------------------------\n");
   for(int x=startValue; x<endValue; x++)
   {
      printf("%2d   %3d\n", x, (*fp)(x));
   }
}

int cube(int x) {
   return x*x*x;
}

int main()
{
   squaredValues(1, 10, square);
   cubedValues(1, 10, cube);
    
   return 0;
} 

