#include <stdio.h>

int main() 
{
   // a data value and an array 
   int value, array[10]; 

   // point to the first element 
   int *arrptr = &array[0];
   printf("arrptr: %d\n", arrptr);
   
   // get element #0 from arrptr 
   value = *arrptr++; 
   printf("value1: %d\n", value);

   value = *++arrptr; 
   printf("value2: %d\n", value);

   // get element #1 from arrptr 
   value = ++*arrptr; 
   printf("value3: %d\n", value);
}   

