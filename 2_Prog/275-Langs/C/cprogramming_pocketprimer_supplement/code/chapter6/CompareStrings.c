#include <stdio.h>
#include <string.h>

int main()
{
   char *str1 = "abc";
   char *str2 = "abcd";

   int num = strcmp(str1, str2);

   printf("String1: %s\n", str1);
   printf("String2: %s\n", str2);

   if(strcmp(str1, str2) == 0 )
   {
      printf("Strings are equal: %s %s\n", str1, str2);
   }
   else if(strcmp(str1, str2) < 0 )
   {
      printf("First < second:    %s %s\n", str1, str2);
   }
   else
   {
      printf("First > second:    %s %s\n", str1, str2);
   }

   return 0;
}

