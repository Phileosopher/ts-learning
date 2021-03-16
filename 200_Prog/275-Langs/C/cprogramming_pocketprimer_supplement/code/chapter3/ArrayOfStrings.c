#include <stdio.h>
#include <string.h>

int main()
{
   char names[3][20];
   strcpy(names[0], "Jane Smith");
   strcpy(names[1], "John Edwards");
   strcpy(names[2], "Steve Anderson");

   for(int i=0; i<3; i++) 
   {
      printf("Name: %s\n", names[i]);
   }

   return 0;
}

