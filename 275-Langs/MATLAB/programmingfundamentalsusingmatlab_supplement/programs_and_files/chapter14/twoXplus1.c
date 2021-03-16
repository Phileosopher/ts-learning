/*
   twoXplus1.c

   Simple example of a C program: find 2 * x + 1.
   
   -Michael Weeks

   This code contains some lines from YPRIME.C, which
   is an example provided by MATLAB. Some variable
   names (m, n, nlhs, plhs, nrhs, prhs) are the same
   as in YPRIME.C. Note that nlhs, plhs, nrhs, prhs also appear
   in the declaration of mexFunction, in mex.h.
   I assume that these variables stand for the following.
     nlhs - number of left-hand side arguments
     plhs - pointer to left-hand side arguments
     nrhs - number of right-hand side arguments
     prhs - pointer to right-hand side arguments

   The include file can be found here:
   /Applications/MATLAB_R2016b.app/extern/include/mex.h

   The "mex.h" include file declares the "mexFunction", "mexErrMsgIdAndTxt".
   "matrix.h" declares "mxGetPr", "mxSetPr", "mxGetM", "mxGetN"
     and "mxCreateDoubleMatrix".
   "tmwtypes.h" defines "mwSize"

*/

// Start of lines from YPRIME.C.
#include "mex.h"

void mexFunction(int nlhs, mxArray *plhs[], 
                 int nrhs, const mxArray *prhs[]) {

    size_t m, n; 
// End of lines from YPRIME.C.
    //   size_t is a positive integer type, defined in C/C++
    //   mwSize is also a positive integer type, and be exactly the same,
    //   though mwSize is a MATLAB-defined type.

    int r, c;
    double *myinputs;
    double *myoutputs;

    // The next line is from YPRIME.C, and the following lines are similar
    // to lines in that program.
    /* Check for proper number of input and output arguments */    
    if (nrhs != 1) {
        mexErrMsgIdAndTxt("MATLAB:mexevalstring:nInput", 
          "Expecting an input argument.");
    } 
    if (nlhs > 1) {
        mexErrMsgIdAndTxt("MATLAB:mexevalstring:nOutput", 
          "There should be zero or one output argument.");
    } 

    // Get the size of the input argument.
    // Lines are similar to YPRIME.C
    m = mxGetM(prhs[0]);    // mxGetM gets the number of rows
    n = mxGetN(prhs[0]);    // mxGetN gets the number of columns 

    // Comment below is from YPRIME.C, mxCreateDoubleMatrix line is similar.
    /* Create a matrix for the return argument */ 
    // Make the return argument the same size as the input argument.
    //   mwSize is a positive integer type
    plhs[0] = mxCreateDoubleMatrix( (mwSize)m, (mwSize)n, mxREAL); 

    // Get the input and output parameters as pointers.
    //  See also mxArray and mxGetData
    myinputs = mxGetPr(prhs[0]);    // Get a pointer to real data
    myoutputs = mxGetPr(plhs[0]);   // Get a pointer to real data

    // For each input(r,c), calculate the output(r,c).
    for (r=0; r<m; r++) {
        for (c=0; c<n; c++) {
            // m rows by n columns
            // calculate output = 2*input + 1
            myoutputs[c*m + r] = 2 * myinputs[c*m + r] + 1;
            // Note: for this example, the following would also work.
            // myoutputs[r*n + c] = 2 * myinputs[r*n + c] + 1;
        }
    }
}

