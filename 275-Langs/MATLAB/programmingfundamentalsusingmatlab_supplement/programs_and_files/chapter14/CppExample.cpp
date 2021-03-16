/*
   CppExample.cpp

   Simple example of a C++ program: find 2 * x + 1.
   
   -Michael Weeks

*/
#include <iostream>

using namespace std;

int main(int argc, char *myinputs[]) {

    if (argc < 2) {
        cout << "Expecting an input argument." << endl; 
        exit(-1);
    }   

    int c;
    double currentInput;
    double myoutput;

    // For each input(c), calculate the output(c).
    for (c=1; c<argc; c++) {
        currentInput = atof(myinputs[c]);
        // calculate output = 2*input + 1
        myoutput = 2 * currentInput + 1;
        cout << myoutput << endl;
    }

    return 0;
}

