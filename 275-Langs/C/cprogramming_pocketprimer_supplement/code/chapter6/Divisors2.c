#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
   char *primes, prime[20];
   int div=2, num=12;

   printf("Number: %d\n", num);

   while(num > 1)
   {
      if(num % div == 0)
      {
         // convert number to string
         sprintf(prime, "%d", div);

         // append string to main string
         asprintf(&primes, "%s %s", primes, prime);

         num /= div;
      }
      else
      {
        ++div;
      }
   }

   printf("Divisors: %s\n", primes);

   return 0;
}

