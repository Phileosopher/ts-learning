#include <ctype.h>
#include <stdio.h>

void findChar(char str[], char c)
{
   int matchCount = 0;

   printf("String: %s\n",str);
   printf("Char:   %c\n",c);

   for(int i=0; str[i]; i++)
   {
      if(str[i] == c)
      {
         printf("Match in position: %d\n",i);
         ++matchCount;
      }
   }

   printf("Count:  %d\n\n",matchCount);
}

int main(int argc, char **argv)
{
   char str1[] = "pasta";
   findChar(str1, 'a');

   char str2[] = "New York City";
   findChar(str2, 'k');

   char str3[] = "California";
   findChar(str3, 'z');
}

