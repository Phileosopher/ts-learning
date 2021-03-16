#include <stdio.h>
#include <string.h>

int main()
{
   char *str = "thisisalongstring";
   int len = strlen(str);

   for(int i=1; i<=len; i++)
   {
      for(int j=0; j<i; j++)
      {
         printf("%c", (char)str[j]);
      }
      for(int j=0; j<len-i; j++)
      {
         printf("*");
      }
      printf("\n");
   }
    
   return 0;
}

