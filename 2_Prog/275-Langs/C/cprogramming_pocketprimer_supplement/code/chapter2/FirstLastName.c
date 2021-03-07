#include <stdio.h>
#include <string.h>

char first[100]; 
char last[100];  
char full[200];

int main() 
{
   printf("Enter first name: ");
   fgets(first, sizeof(first), stdin);

   // why is this here?
   first[strlen(first)-1] = '\0';
 
   printf("Enter last name: "); 
   fgets(last, sizeof(last), stdin);
   
   strcpy(full, first); strcat(full, " "); 
   strcat(full, last);
   
   printf("The name is %s\n", full); 
   
   return (0);
}

