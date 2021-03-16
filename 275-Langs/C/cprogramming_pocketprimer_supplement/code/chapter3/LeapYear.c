#include <stdio.h>

int main()
{
   int years[6] = {1900, 1953, 1958, 2000, 2004, 2006};
   int year=0, leapyear=0;

   int len = sizeof(years)/sizeof(years[0]);

   for(int i=0; i<len; i++) 
   {
      year = years[i];

      if( year % 4 == 0)
      {
         leapyear = 1;

         // "leap centuries" must be multiples of 400
         if( (year % 100 == 0) && (year % 400 != 0) )
         {
            leapyear = 0;
         }
      }
      else 
      {
         leapyear = 0;
      }

      if( leapyear == 0)
      {
         printf("%d: not a leap year\n",year);
      }
      else
      {
         printf("%d: leap year\n",year);
      }
   }

   return 0;
}

