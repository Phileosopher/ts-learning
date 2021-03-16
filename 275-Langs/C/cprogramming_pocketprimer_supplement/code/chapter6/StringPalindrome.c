#include <stdio.h>
#include <string.h>

int scanString(char str[])
{
   int result = 0;
   char *ptr;
   int len = strlen(str);

   for(int i=0; i<len/2; i++)
   {
      if(str[i] != str[len-i-1])
      {
         result = 1; 
         break;
      }
   }

   return result;
}

int main()
{
   int result=0;
   char line1[] = "radar";
   char line2[] = "motion";
   char *results[2] = {"YES", "NO"};

   int len1 = strlen(line1);
   int len2 = strlen(line2);

   result = scanString(line1);
   printf("Current Word: %s\n", line1);
   printf("Palindrome:   %s\n", results[result]);

   result = scanString(line2);
   printf("Current Word: %s\n", line2);
   printf("Palindrome:   %s\n", results[result]);
    
   return 0;
}

