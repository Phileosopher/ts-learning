#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
   char ch, line[] = "Abc3 :";
   int i, count;

   count = strlen(line);

   for(i=0; i<count; i++) 
   {
     ch = line[i];

     if(isblank(ch))
     {
        printf("%c is a blank\n", ch);
     }
     else if(isdigit(ch))
     {
        printf("%c is a digit\n", ch);
     }
     else if(isupper(ch))
     {
        printf("%c is uppercase\n", ch);
     }
     else if(islower(ch))
     {
        printf("%c is uppercase\n", ch);
     }
     else if(ispunct(ch))
     {
        printf("%c is punctuation\n", ch);
     }
     else
     {
        printf("%c is other type\n", ch);
     }
   }

   return 0;
}

