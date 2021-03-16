#include <stdio.h>

float perimeter(width, height) 
int width;
float height;
{
   return (width * height); 
}

int main(int argc, char **argv)
{
   float perim = perimeter(10.0, 5);
   printf("Perimeter = %f\n", perim);
   return (0); 
}

