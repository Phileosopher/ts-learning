#include <stdio.h>
#include <string.h>

char first[100];
char last[100];
char fullName[200];

int main()
{
   strcpy(first, "John");
   strcpy(last,  "Smith");
   strcpy(fullName, first);

   strcat(fullName, " ");
   strcat(fullName, last);
   printf("The full name is %s\n", fullName);

   return 0;
}

