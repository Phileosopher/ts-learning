#include <stdio.h>

int main()
{
   char *ptr1  = "Hello World";
   char str1[] = "Hello World";
   char *ptr2  = str1;

   printf("%s\n", ptr1);
   printf("%s\n", str1);
   printf("%s\n", ptr2);

   return 0;
}

