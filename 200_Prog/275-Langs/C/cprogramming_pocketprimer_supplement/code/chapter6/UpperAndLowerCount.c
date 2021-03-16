#define _POSIX_C_SOURCE 200809L 
#define __STDC_WANT_LIB_EXT1__ 1 
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
 
//------------------------------------------------------------------
// As with all bounds-checked functions, strncpy_s is only guaranteed 
// to be available if __STDC_LIB_EXT1__ is defined by the implementation 
// and if the user defines __STDC_WANT_LIB_EXT1__ to the integer constant 
// 1 before including string.h.
// gcc -D_POSIX_C_SOURCE=200809L CopyFunction2.c -o CopyFunction2 
//------------------------------------------------------------------

int main()
{
   char str1[] = "This is a String";
   char *lower1, *upper1;
   int lcount=0, ucount=0;

   int len1 = strlen(str1);
   lower1 = (char *)malloc(len1);
   upper1 = (char *)malloc(len1);

   for(int i=0; i<len1; i++)
   {
      if(str1[i] == tolower(str1[i]))
      {
         *(lower1+lcount) = str1[i];
         lcount++;
      }
      else if(str1[i] == toupper(str1[i]))
      {
         *(upper1+ucount) = str1[i];
         ucount++;
      }
/*
      // correct code:
      if(islower(str1[i]))
      {
         *(lower1+lcount) = str1[i];
         lcount++;
      }
      else if(isupper(str1[i]))
      {
         *(upper1+ucount) = str1[i];
         ucount++;
      }
*/
   }

   *(lower1+lcount) = '\0';
   *(upper1+ucount) = '\0';

   printf("Original:  %s\n",str1);
   printf("Lowercase: %s\n",lower1);
   printf("Uppercase: %s\n",upper1);

   return 0;
}

