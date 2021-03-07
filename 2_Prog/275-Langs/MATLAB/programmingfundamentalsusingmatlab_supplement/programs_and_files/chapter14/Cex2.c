/*
   Cex2.c

   Simple example of a C program
   
   -Michael Weeks

*/

// Start of lines from YPRIME.C.
#include "mex.h"

void mexFunction(int nlhs, mxArray *plhs[], 
                 int nrhs, const mxArray *prhs[]) {

    size_t m, n; 
// End of lines from YPRIME.C.

    int r, c;
    double *myinputs;
    double *myoutputs;

    // Get the size of the input argument.
    // Lines are similar to YPRIME.C
    m = mxGetM(prhs[0]);    // mxGetM gets the number of rows
    n = mxGetN(prhs[0]);    // mxGetN gets the number of columns 

    // Comment below is from YPRIME.C, mxCreateDoubleMatrix line is similar.
    /* Create a matrix for the return argument */ 
    // Make the return argument the same size as the input argument.
    //   mwSize is a positive integer type
//    plhs[0] = mxCreateDoubleMatrix( (mwSize)m, (mwSize)n, mxREAL); 

    // Get the input and output parameters as pointers.
    //  See also mxArray and mxGetData
    myinputs = mxGetPr(prhs[0]);    // Get a pointer to real data
//    myoutputs = mxGetPr(plhs[0]);   // Get a pointer to real data

    printf("There are %d rows x %d columns of inputs\n", m, n);
    // For each input(r,c), calculate the output(r,c).
    // Just echo back the input.
    for (r=0; r<m; r++) {
        for (c=0; c<n; c++) {
            // m rows by n columns
            // calculate output = 2*input + 1
            printf(" %5.2f ", myinputs[c*m + r]);
        }
        printf("\n");
    }
    printf("\n");
}

