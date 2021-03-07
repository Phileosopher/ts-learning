echo "Compiling ArrayAndPointer1.c"
gcc -std=c11 ArrayAndPointer1.c       -o ArrayAndPointer1
echo "Compiling ConcatenateStrings.c"
gcc -std=c11 ConcatenateStrings.c     -o ConcatenateStrings
echo "Compiling AbsValues.c"
gcc -std=c11 CountVowelsConsonants.c  -o CountVowelsConsonants
echo "Compiling FindChar1.c"
gcc -std=c11 FindChar1.c              -o FindChar1
echo "Compiling ForLoopStr.c"
gcc -std=c11 ForLoopStr.c             -o ForLoopStr
echo "Compiling PointerArithmetic.c"
gcc -std=c11 PointerArithmetic.c      -o PointerArithmetic
echo "Compiling PointerNumbers1.c"
gcc -std=c11 PointersNumbers1.c       -o PointersNumbers1
echo "Compiling PointerNumbers2.c"
gcc -std=c11 PointersNumbers2.c       -o PointersNumbers2
echo "Compiling PointersStrings1.c"
gcc -std=c11 PointersStrings1.c       -o PointersStrings1
echo "Compiling PointersToNumbers1.c"
gcc -std=c11 PointersToNumbers1.c     -o PointersToNumbers1
echo "Compiling PrintCmdLineArguments.c"
gcc -std=c11 PrintCmdLineArguments.c  -o PrintCmdLineArguments
echo "Compiling SearchForWordInString.c"
gcc -std=c11 SearchForWordInString.c  -o SearchForWordInString
echo "Compiling SimplePointer1.c"
gcc -std=c11 SimplePointer1.c         -o SimplePointer1
echo "Compiling SimplePointer2.c"
gcc -std=c11 SimplePointer2.c         -o SimplePointer2
echo "Compiling SimplePointer3.c"
gcc -std=c11 SimplePointer3.c         -o SimplePointer3
echo "Compiling SimpleString.c"
gcc -std=c11 SimpleString.c           -o SimpleString
echo "Compiling Substrings.c"
gcc -std=c11 Substrings.c             -o Substrings
echo "Compiling Transpose.c"
gcc -std=c11 Transpose.c              -o Transpose

echo ""
echo "Files containing strcpy:"
grep -l strcpy *.c

echo ""
echo "Files containing strncpy:"
grep -l strncpy *.c

