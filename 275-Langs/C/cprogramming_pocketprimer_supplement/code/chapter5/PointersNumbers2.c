#include <stdio.h>

#define ARRAY_SIZE 10
char array[ARRAY_SIZE + 1] = "0123456789";

int main()
{
  int index;
  printf("&array[index] (array+index) array[index]\n");

  for(index=0; index < ARRAY_SIZE; ++index) {
    printf("0x%-10p 0x%-10p 0x%x\n",
           &array[index],(array+index),array[index]);
  }

  return 0;
}

