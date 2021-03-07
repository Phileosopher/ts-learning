#include <stdio.h>
#include <string.h>

union MyData
{
   int i;
   float f;
   char str[10];
};

int main(int argc, char **argv)
{
   union MyData mydata;
   printf("Memory allocated to mydata: ");
   printf("%zu %zu %zu\n", sizeof (mydata.i), sizeof (mydata.f), sizeof (mydata.str));
   return 0;
}

