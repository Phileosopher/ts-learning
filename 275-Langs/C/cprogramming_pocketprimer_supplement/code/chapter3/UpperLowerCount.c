#include <stdio.h>
#include <string.h>
 
int main()
{
   char ch, str1[] = "This is a String";
   int lcount=0, ucount=0;

   int len1 = strlen(str1);

   for(int i=0; i<len1; i++)
   {
      ch = str1[i];
      if( ('a' <= ch) && (ch <= 'z')) 
      {
         lcount++;
      }
      else if( ('A' <= ch) && (ch <= 'Z')) 
      {
         ucount++;
      }
   }

   printf("Original:    %s\n",str1);
   printf("Lower count: %d\n",lcount);
   printf("Upper count: %d\n",ucount);

   return 0;
}

