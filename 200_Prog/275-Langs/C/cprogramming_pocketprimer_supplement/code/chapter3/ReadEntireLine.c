#include <stdio.h>

#define LINE_SIZE 100

int main()
{
   int charCount=0, inputChar;
   char line[LINE_SIZE];
   char lineFeed = '\n';

   while( (inputChar = getchar()) != lineFeed )
   {
      if(charCount < LINE_SIZE)
      {
         line[charCount] = inputChar;
      }

      charCount++;
   }

   printf("Input length = %d\n", charCount);

   return 0;
}

