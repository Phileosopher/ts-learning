#include <stdio.h>

// prevent "Implicit declaration of function is invalid in C99"
void message();

int main()
{
   message();

   return 0;
}

void message()
{
   printf("Hello from message\n");
}

