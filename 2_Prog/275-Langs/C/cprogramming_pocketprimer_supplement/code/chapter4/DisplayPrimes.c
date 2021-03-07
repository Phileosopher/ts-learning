#include<stdio.h>

int isPrime(int idx)
{
   int flag=0, div=2;
   while (div <= idx/2)
   { 
      if (idx % div == 0) // composite
      {  
         flag = 1; 
         break;
      } 
      div++;
   } 

   return flag;
}

int main()
{ 
   int maxVal=50, idx=0, result=0;

   for (idx=1; idx<=maxVal; idx++)
   {
      result = isPrime(idx);

      if ( result == 0) // prime 
      {
         printf("%d ", idx);
      }
   }

   return 0;
}

