#include <stdio.h>

int main()
{
   char *str  = "thisisalongstring";

   char *ptr1 = (char *)&str;    // incorrect
   char *ptr2 = (char *)&str[0];
   char *ptr3 = &str[0];
   char *ptr4 = str; 
 //char *ptr5 = &str;            // <= warning

   printf("str:  %s\n", str);
 //printf("ptr1: %s\n", ptr1);
   printf("ptr2: %s\n", ptr2);
   printf("ptr3: %s\n", ptr3);
   printf("ptr4: %s\n", ptr4);
 //printf("ptr5: %s\n", ptr5);
  
   return 0;
}

