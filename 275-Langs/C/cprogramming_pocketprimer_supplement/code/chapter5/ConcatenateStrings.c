#include <stdio.h>
#include <string.h>

#define BUFFER_SIZE 80

int main()
{	
  char line[BUFFER_SIZE] = "New York";
  char *ptr;

  // Call strcat with line and " pizza"
  ptr = strcat(line, " pizza" );
  printf("strcat line  = %s\n", line);

  // Reset line to contain the original string
  memset(line, '\0', sizeof( line));
  ptr = strcpy(line, "New York");
  strcpy(line, "New York");

  // Call strncat with line and "pizza"
  ptr = strncat(line, " pizza", 3);
  printf("strncat line = %s\n", line);

  return 0;
}

