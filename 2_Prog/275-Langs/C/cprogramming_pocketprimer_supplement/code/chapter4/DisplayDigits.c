#include <ctype.h>
#include <stdio.h>

void checkDigits(char str[])
{
   printf("Number: %s\n",str);

   for(int i=0; str[i]; i++)
   {
      if(isdigit(str[i]))
      {
         printf("Digit: %c\n",str[i]);
      }
      else
      {
         printf("Not Digit: %c\n",str[i]);
      }
   }

   printf("\n");
}

int main(int argc, char **argv)
{
   char str1[] = "123.456";
   checkDigits(str1);
   char str2[] = "-51.203";
   checkDigits(str2);
}

