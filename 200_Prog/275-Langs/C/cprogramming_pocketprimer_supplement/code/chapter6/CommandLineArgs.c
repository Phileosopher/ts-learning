#include <stdio.h>

int main(int argc, char **argv)
{
   char *ptr;

   for(int i=0; i<argc; i++) 
   {
      ptr = argv[i];
      printf("Position:  %d\n",i);
      printf("Argument:  %s\n",ptr);
   }

   return 0;
}

