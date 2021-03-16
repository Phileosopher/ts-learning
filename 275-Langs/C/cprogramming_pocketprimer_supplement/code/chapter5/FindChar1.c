#include <stdio.h>
#include <string.h>

#define SIZE 80

int main(void)
{
  char line[SIZE] = "New York Pizza";
  char *ptr;
  int ch = 'z';

  ptr = strchr(line, ch);
  printf("The first occurrence of %c in '%s' is '%s'\n",
          ch, line, ptr);

  return 0;
}

