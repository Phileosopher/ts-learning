#include <stdio.h>
#include <string.h>

int main()
{
   char *str = "One two Three four";
   char *word1 = "our";
   char *word2 = "three";

   if((strstr(str, word1)) != NULL)
   {
      printf("Current Line: %s\n", str);
      printf("Exact Match:  %s\n\n", word1);
   }

   return 0;
}

