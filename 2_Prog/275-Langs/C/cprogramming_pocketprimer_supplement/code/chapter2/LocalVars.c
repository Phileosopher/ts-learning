#include <stdio.h>

// global variable declaration
int a=1, b=2, c=3;

void printGlobalVariables()
{
  printf ("Inside the printGlobalVariables function\n");
  printf ("GLOBAL value of a = %d, b = %d and c = %d\n", a, b, c);
}

int main()
{
  printf ("GLOBAL value of a = %d, b = %d and c = %d\n", a, b, c);

  // local variable declaration
  int a, b, c;

  // actual initialization
  a = 10;
  b = 20;
  c = a + b;

  printf ("LOCAL value of a = %d, b = %d and c = %d\n", a, b, c);

  printGlobalVariables();

  return 0;
}

