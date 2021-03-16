#include <stdio.h>
#include <ctype.h>

int main()
{
   int ch;

   for (ch = 0x7c; ch <= 0x82; ch++) {
      printf("%#04x    ", ch);

      if (isascii(ch))
      {
         printf("The character is %c\n", ch);
      }
      else
      {
         printf("Cannot be represented by an ASCII character\n");
      }
   }

   return 0;
}

