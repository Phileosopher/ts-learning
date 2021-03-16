#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() 
{
   char * ls_args[] = { "/bin/ls" , "-l", NULL};

   int pid = fork();

   if(pid == 0) // the child 
   {
      execv(ls_args[0], ls_args);
   } 
   else if(pid > 0) // the parent 
   { 
      // wait for the child to complete 
      wait(NULL);
   }
   else 
   { 
      printf("Error: negative process ID\n");
   }

   return 0;
}

