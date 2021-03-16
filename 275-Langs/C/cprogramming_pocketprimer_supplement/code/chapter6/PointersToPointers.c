#include <stdio.h>

int main()
{
   char *list[] = {"a", "b", "c", "d", NULL};

   for (char **ptr=list; *ptr != NULL; ptr++){
       printf("array item: %s\n", ptr[0]);
   }

   return 0;
}

