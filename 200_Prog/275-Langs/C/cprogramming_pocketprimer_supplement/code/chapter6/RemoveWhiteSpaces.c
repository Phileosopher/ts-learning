#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
 
int main()
{
   char str1[] = "This is a String";
   char *ptr1;
   int count=0;

   int len1 = strlen(str1);
   ptr1= (char *)malloc(len1);

   for(int i=0; i<len1; i++)
   {
      if((str1[i] == ' ') || (str1[i] == '\t')) 
      {
         continue;
      }
      else
      {
         *(ptr1+count) = str1[i];
         count++;
      }
   }

   *(ptr1+count) = '\0';

   printf("Original:  %s\n",str1);
   printf("Stripped:  %s\n",ptr1);

   return 0;
}

