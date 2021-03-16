#include <ctype.h>
#include <stdio.h>

void findChar(char str[], char c)
{
   int matchCount = 0;

   printf("String: %s\n",str);
   printf("Char:   %c\n",c);

   for(int i=0; str[i]; i++)
   {
      if(str[i] == c)
      {
         printf("Match in position: %d\n",i);
         ++matchCount;
      }
   }

   printf("Count:  %d\n\n",matchCount);
}

