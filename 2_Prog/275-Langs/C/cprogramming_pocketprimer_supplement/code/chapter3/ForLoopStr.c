
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
   char *str = "hello";
   char *p = str;
   int len = strlen(str);

   printf("First Loop\n");
   printf("----------\n");
   for(int i=0; i<len; i++)
   {
      printf("i : %c\n", (char)str[i]);
   }

   printf("\nSecond Loop\n");
   printf("-----------\n");
   for(int i=0; i<len; i++)
   {
      printf("i : %s\n", (char *)p);
      ++p;
   }

   return 0;
}

