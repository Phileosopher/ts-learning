#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
   char str1[] = "  This is a   String";
   int i=0, wCount=0;

   int len1 = strlen(str1);

   // skip over leading whitespace 
   for(i=0; i<len1; i++) 
   {
     if((str1[i]!=' ')&&(str1[i]!='\t'))
     {
        break;
     }
   }

   for(; i<len1; i++)
   {
      // found a whitespace => found a word
      if((str1[i]==' ')||(str1[i]=='\t'))
      {
         wCount++;
      }

      // handle the case where there are
      // multiple whitespaces between words
   }

   wCount++;

   printf("Line of Text:  %s\n",str1);
   printf("Word Count:    %d\n",wCount);

   return 0;
}

