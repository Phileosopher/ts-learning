echo "Compiling ArrayOfPointers.c"
gcc -std=c11 ArrayOfPointers.c             -o ArrayOfPointers
echo "Compiling CharCounts.c"
gcc -std=c11 CharCounts.c                  -o CharCounts
echo "Compiling CompareStrings.c"
gcc -std=c11 CompareStrings.c              -o CompareStrings
echo "Compiling CopyFunction2.c"
gcc -std=c11 CopyFunction2.c               -o CopyFunction2
echo "Compiling Divisors2.c"
gcc -std=c11 Divisors2.c                   -o Divisors2
echo "Compiling FunctionPointersAsArgs.c"
gcc -std=c11 FunctionPointersAsArgs.c      -o FunctionPointersAsArgs
echo "Compiling JaggArrays.c"
gcc -std=c11 JaggedArrays.c                -o JaggedArrays
echo "Compiling MallocFree.c"
gcc -std=c11 MallocFree.c                  -o MallocFree
echo "Compiling PalinDromes1.c"
gcc -std=c11 PalinDromes1.c                -o PalinDromes1
echo "Compiling PassByPointer.c"    
gcc -std=c11 PassByPointer.c               -o PassByPointer
echo "Compiling PassArrayByPointer.c"
gcc -std=c11 PassArrayByPointer.c          -o PassArrayByPointer
echo "Compiling PointersAndFunctions.c"
gcc -std=c11 PointersAndFunctions.c        -o PointersAndFunctions
echo "Compiling PointersArrayNums1.c"
gcc -std=c11 PointersArrayNums1.c          -o PointersArrayNums1
echo "Compiling PointersDecimals1.c"
gcc -std=c11 PointersDecimals1.c           -o PointersDecimals1
echo "Compiling PointersToNonVoidFunctions1.c"
gcc -std=c11 PointersToNonVoidFunctions1.c -o PointersToNonVoidFunctions1
echo "Compiling PointersToPointers.c"
gcc -std=c11 PointersToPointers.c          -o PointersToPointers
echo "Compiling PointersToVoidFunctions1.c"
gcc -std=c11 PointersToVoidFunctions1.c    -o PointersToVoidFunctions1
echo "Compiling RemoveWhiteSpaces.c"
gcc -std=c11 RemoveWhiteSpaces.c           -o RemoveWhiteSpaces
echo "Compiling ReverseArrayNums1.c"
gcc -std=c11 ReverseArrayNums1.c           -o ReverseArrayNums1
echo "Compiling ReverseString1.c"
gcc -std=c11 ReverseString1.c              -o ReverseString1
echo "Compiling SytringPalindrome.c"
gcc -std=c11 StringPalindrome.c            -o StringPalindrome
echo "Compiling Tokenize.c"
gcc -std=c11 Tokenize.c                    -o Tokenize
echo "Compiling UpperAndLowerCount.c"
gcc -std=c11 UpperAndLowerCount.c          -o UpperAndLowerCount
echo "Compiling UpperLowerCase.c"
gcc -std=c11 UpperLowerCase.c              -o UpperLowerCase

echo ""
echo "Files containing strcpy:"
grep -l strcpy *.c

echo ""
echo "Files containing strncpy:"
grep -l strncpy *.c

