/*
   Cexample.c

   Simple example of a C program: find 2 * x + 1.
   
   -Michael Weeks

*/

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *myinputs[]) {

    if (argc < 2) {
        printf("Expecting an input argument.\n"); 
        exit(-1);
    }   
    // if (argc == 2) {
    //     printf("Using number '%s'.\n", myinputs[1]); // argv[1]);
    // }

    int c;
    double currentInput;
    double myoutput;

    // Get the input argument.

    // For each input(c), calculate the output(c).
    for (c=1; c<argc; c++) {
        currentInput = atof(myinputs[c]);
        // printf("Current input is %5.2f \n", currentInput);
        // calculate output = 2*input + 1
        myoutput = 2 * currentInput + 1;
        printf("%5.2f \n", myoutput);
    }

    return 0;
}

