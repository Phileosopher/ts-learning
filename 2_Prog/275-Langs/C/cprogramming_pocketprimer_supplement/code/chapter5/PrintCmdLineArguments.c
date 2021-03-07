#include <stdio.h>

// argc is the number of arguments and argv is the argument array

int main(int argc, char * argv[]) 
{
   int i;

   printf("Display Command Line Arguments\n");
   for( i = 0; i < argc; ++i ) 
   {
      printf("Argument %d = \"%s\"\n", i, argv[i]);
   }

   return 0;
}

