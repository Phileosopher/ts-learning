#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main()
{
   char *src = "This Is A Line";
   char *lower, *upper, *chr;
   int len;
   len = strlen(src);

   lower = (char *)malloc(sizeof(src));
   strncpy(lower, src, len);
 //strncpy_s(lower, len, src, len);
   lower[len-1] = '\0';

   upper = (char *)malloc(sizeof(src));
   strncpy(upper, src, len);
 //strncpy_s(lower, len, src, len);
   upper[len-1] = '\0';

   for(int i=0; i<len; i++)
   {	
      *(lower+i) = tolower(src[i]);
      *(upper+i) = toupper(src[i]);
   }

   printf("Original: %s\n", src);
   printf("Upper:    %s\n", upper);
   printf("Lower:    %s\n", lower);
}

