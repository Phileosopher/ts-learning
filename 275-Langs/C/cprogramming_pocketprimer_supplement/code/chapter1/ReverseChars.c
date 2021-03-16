#include <stdio.h>

char char1; char char2; char char3;

int main() 
{
   // first character 
   char1 = 'A';

   // second character
   char2 = 'B';

   // third character
   char3 = 'C';

   printf("%c%c%c reversed is %c%c%c\n",
           char1, char2, char3,
           char3, char2, char1); 

   return (0);
}

