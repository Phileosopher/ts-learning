#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int charType(char ch)
{
   char ch2 = tolower(ch);
 
   if(ch2 =='a' ||ch2 =='e' ||ch2 =='i' ||ch2 =='o' || ch2 =='u')
   {
     return 0;
   }
   else if(isalpha(ch2))
   {
     return 1;
   }
   else if(isdigit(ch2))
   {
     return 2;
   }
   else 
   {
     return 3;
   }
}

int main()
{
   char str[] = "This is a string with some short words 1 2 3 4 that wraps around and let's see how well the code in this code sample actually works!";

   char *ptr = str;

   int result, counts[4];
   counts[0] = counts[1] = counts[2] = counts[3] = 0;
 
   while(*ptr)
   {
      result = charType(*ptr);
      ++counts[result];
      ptr++;
   }
    
   printf("VOWELS:    %d\n",counts[0]); 
   printf("CONSONANT: %d\n",counts[1]); 
   printf("DIGITS:    %d\n",counts[2]); 
   printf("OTHERS:    %d\n",counts[3]); 

   return 0;
}

