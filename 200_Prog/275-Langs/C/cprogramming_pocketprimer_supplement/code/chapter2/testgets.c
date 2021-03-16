// C program to illustrate gets()
#include <stdio.h>
#define MAX 10
 
int main()
{
   char buf[MAX];
 
   printf("Enter a string: ");
   gets(buf);
   printf("string is: %s\n", buf);
 
   return 0;
}
