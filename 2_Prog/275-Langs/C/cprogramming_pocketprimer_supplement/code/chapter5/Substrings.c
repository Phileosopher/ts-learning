#include <stdio.h>
#include <string.h>

int main()
{
   char *str = "thisisalongstring";
   int len = strlen(str);

   for(int i=1; i<=len; i++)
   {
      printf("%2d: ",i);
      for(int j=0; j<i; j++)
      {
         printf("%c", (char)str[j]);
      }
      printf("\n");
   }
  
   return 0;
}

