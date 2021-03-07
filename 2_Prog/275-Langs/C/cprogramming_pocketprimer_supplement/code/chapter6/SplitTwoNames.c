#include <stdio.h>
#include <string.h>

int main() 
{
   char *str = "Smith/John";
   const char ch = '/';
   char *first = (char *)str;
   char *second;
   char *result;

   result = strchr(str, ch);
   printf("string = %s\n", str);
   printf("result = %s\n", result);

   second = (char *)result;
   printf("first  = %s\n", first);
   printf("second = %s\n", second);

   // skip the "/" symbol:
   ++result; 
   printf("result = %s\n", result);

   // how do we find the first name?
    
   return 0;
}

