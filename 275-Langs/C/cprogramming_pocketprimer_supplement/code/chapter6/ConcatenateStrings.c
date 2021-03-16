#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int main()
{
   char str1[] = "String one ";
   char str2[] = "This is string two";
   char *ptr1;

   int len1 = strlen(str1);
   int len2 = strlen(str2);
   int len3 = len1+len2+1;
   ptr1 = (char *)malloc(len3);

   ptr1 = str1;
   strcat(ptr1, str2);
   *(ptr1+len3-1) = '\0';

   printf("Concatenation: %s\n",str1);

   return 0;
}

