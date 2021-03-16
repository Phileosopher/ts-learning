#include <stdlib.h>
#include <stdio.h>
 
int main(int argc, char **argv)
{
   char *pathvar;
 
   pathvar = getenv("PATH");
   printf("pathvar=%s",pathvar);
}

