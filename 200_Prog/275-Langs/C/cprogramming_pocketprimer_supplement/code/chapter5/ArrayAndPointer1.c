#include <stdio.h>

int main(){
   int numbers[5] = {2, 3, 5, 7, 11};
   printf("First item in numbers  = %i\n", *numbers);

   int *numbers2 = &numbers[1];
   printf("First item in numbers2 = %i\n", numbers2[0]);

   return 0;
}   

