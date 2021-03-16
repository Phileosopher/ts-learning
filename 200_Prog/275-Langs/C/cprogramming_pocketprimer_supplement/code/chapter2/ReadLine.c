#include <string.h>
#include <stdio.h>

char line[100]; 

int main() 
{
  printf("Enter a line: ");
  fgets(line, sizeof(line), stdin);
  printf("The length of the line is: %d\n", strlen(line));

  return (0);
}

