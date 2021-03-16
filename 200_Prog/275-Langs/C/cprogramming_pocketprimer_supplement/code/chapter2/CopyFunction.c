#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 80

int main()
{
  char source[BUFFER_SIZE] = "The initial string";
  char destination[BUFFER_SIZE] = "The target string";
  char *result;

  printf("Before: %s\n", destination);
  result = strcpy(destination, source);
  printf("After:  %s\n", destination);

  return 0;
}

