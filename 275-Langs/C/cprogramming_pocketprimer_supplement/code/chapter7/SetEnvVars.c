#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
   char *pathvar;

   pathvar = getenv("PATH");
   printf("The current path is: %s\n\n", pathvar);

   if (-1 == putenv("PATH=/:/home/userid"))
   {
      printf("putenv failed \n");
      return EXIT_FAILURE;
   }

   pathvar = getenv("PATH");
   printf("The new path is: %s\n", pathvar);

   return 0;
}

