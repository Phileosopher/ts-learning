#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>

int main()
{
   char *filename = "text.txt";

   if (unlink("text.txt") == -1)
   {
      printf("File %s does not exist\n", filename);
   }
   else
   {
      printf("Successfully removed file %s\n", filename);
   }

   return 0;
}

