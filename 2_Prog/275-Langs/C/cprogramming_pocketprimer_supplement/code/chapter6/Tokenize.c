#include <stdio.h>
#include <string.h>
 
char *delim = "/";

void tokenizeString(char *str)
{
   // first token = last name 
   char *token = strtok(str, delim);
   char *second = token;
   char *first;
   int count = 0;
  
   // print token after delimiter
   while (token != NULL)
   {
      first = token;
      token = strtok(NULL, delim);

      if(++count == 1) break;
   }
   printf("NAME: %s %s\n", first, second);
}

int main()
{
   char *str;
   char names[4][20] = {
                        "smith/jane",
                        "edwards/john",
                        "stone/dave",
                        "anderson/kenneth",
                      };

   for(int i=0; i<4; i++)  
   {
      str = names[i];
      tokenizeString(str);
   }

   return 0;
}

