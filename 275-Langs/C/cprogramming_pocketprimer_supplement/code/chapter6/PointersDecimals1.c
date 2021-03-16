#include <stdio.h>

int main()
{
   int ints1[] = {1.0,2.0,3.0,4.0,5.0};
   int *ptr1  = ints1;
   int isize1 = sizeof(ints1)/sizeof(int);

   int floats1[] = {1.0,2.0,3.0,4.0,5.0};
   int *ptr2  = floats1;
   int fsize1 = sizeof(floats1)/sizeof(float);

   double doubles1[] = {1.0,2.0,3.0,4.0,5.0};
   double *ptr3  = doubles1;
   int dsize1 = sizeof(doubles1)/sizeof(double);

   printf("The ints1 array:\n");
   for(int i=0; i<isize1; i++)
   {
      printf("%d ", *(ptr1+i));
   }
   printf("\n");

   for(int i=0; i<isize1; i++)
   {
      printf("%f ", *(ptr1+i));
   }
   printf("\n");

   printf("The floats1 array:\n");
   for(int i=0; i<fsize1; i++)
   {
      printf("%d ", *(ptr2+i));
   }
   printf("\n");

   for(int i=0; i<fsize1; i++)
   {
      printf("%f ", *(ptr2+i));
   }
   printf("\n");

   printf("The doubles1 array:\n");
   for(int i=0; i<dsize1; i++)
   {
      printf("%d ", *(ptr2+i));
   }
   printf("\n");

   for(int i=0; i<dsize1; i++)
   {
      printf("%f ", *(ptr3+i));
   }
   printf("\n");
    
   return 0;
}

