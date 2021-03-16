#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
   char s[256];
   strcpy(s, "One two Three four");
   char* token = strtok(s, " ");

   while (token) {
      printf("token: %s\n", token);
      token = strtok(NULL, " ");
   }

   return 0;
}

