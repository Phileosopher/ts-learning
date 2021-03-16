
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
   char *str = "hello";
   char *p = str;
   int i=0;
   int len = strlen(str);

   printf("First Loop\n");
   printf("----------\n");
   while(i<len)
   {
      printf("i : %c\n", (char)str[i]);
      ++i;
   }

   printf("\nSecond Loop\n");
   printf("-----------\n");
   while(*p)
   {
      printf("char : %s\n", (char *)p);
      ++p;
   }

   return 0;
}

