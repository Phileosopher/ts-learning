#include <stdio.h>

int main()
{   
   char str[100];
   int i, numfilled;

   printf( "Enter a string and an int: ");
   numfilled = scanf("%s %d", str, &i);

   printf("\nNumber of filled values: %d\n",numfilled);
   printf("\nYou entered values for the string and the int");
   printf("\nYou entered the string %s and the number %d\n", str, i);

   return 0;
}

