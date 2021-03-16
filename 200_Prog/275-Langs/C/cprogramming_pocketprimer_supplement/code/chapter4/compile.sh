echo "Compiling AddDigits.c"
gcc -std=c11 AddDigits.c           -o AddDigits
echo "Compiling ComputePower.c"
gcc -std=c11 ComputePower.c        -o ComputePower
echo "Compiling ConvertDataTypes.c"
gcc -std=c11 ConvertDataTypes.c    -o ConvertDataTypes
echo "Compiling CountDigits.c"
gcc -std=c11 CountDigits.c         -o CountDigits
echo "Compiling DisplayDigits.c"
gcc -std=c11 DisplayDigits.c       -o DisplayDigits
echo "Compiling DisplayPrimes.c"
gcc -std=c11 DisplayPrimes.c       -o DisplayPrimes
echo "Compiling Factorial.c"
gcc -std=c11 Factorial.c           -o Factorial
echo "Compiling Fib.c"
gcc -std=c11 Fib.c                 -o Fib
echo "Compiling FindChar1.c"
gcc -std=c11 FindChar1.c           -o FindChar1
echo "Compiling FunctionParams.c"
gcc -std=c11 FunctionParams.c      -o FunctionParams
echo "Compiling GCD.c"
gcc -std=c11 GCD.c                 -o GCD
echo "Compiling LCM.c"
gcc -std=c11 LCM.c                 -o LCM
echo "Compiling OldStyleFunction.c"
gcc -std=c11 OldStyleFunction.c    -o OldStyleFunction
echo "Compiling PrintToBuffer.c"
gcc -std=c11 PrintToBuffer.c       -o PrintToBuffer
echo "Compiling Simplec99.c"
gcc -std=c11 Simplec99.c           -o Simplec99
echo "Compiling SingleArrayFunction.c"
gcc -std=c11 SingleArrayFunction.c -o SingleArrayFunction

echo ""
echo "Files containing strcpy:"
grep -l strcpy *.c

echo ""
echo "Files containing strncpy:"
grep -l strncpy *.c
