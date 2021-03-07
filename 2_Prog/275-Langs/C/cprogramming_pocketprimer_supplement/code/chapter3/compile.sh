echo "Compiling Alphabetic.c"
gcc -std=c11 Alphabetic.c          -o Alphabetic
echo "Compiling ArrayElems.c"
gcc -std=c11 ArrayElems.c          -o ArrayElems
echo "Compiling ArrayOfStrings.c"
gcc -std=c11 ArrayOfStrings.c      -o ArrayOfStrings
echo "Compiling BreakContinue.c"
gcc -std=c11 BreakContinue.c       -o BreakContinue
echo "Compiling CountWords.c"
gcc -std=c11 CountWords.c          -o CountWords
echo "Compiling DeleteArrayElement.c"
gcc -std=c11 DeleteArrayElement.c  -o DeleteArrayElement
echo "Compiling Divisors.c"
gcc -std=c11 Divisors.c            -o Divisors
echo "Compiling Divisors3.c"
gcc -std=c11 Divisors3.c           -o Divisors3
echo "Compiling Factorial2.c"
gcc -std=c11 Factorial2.c          -o Factorial2
echo "Compiling ForLoop.c"
gcc -std=c11 ForLoop.c             -o ForLoop
echo "Compiling ForLoopStr.c"
gcc -std=c11 ForLoopStr.c          -o ForLoopStr
echo "Compiling LeapYear.c"
gcc -std=c11 LeapYear.c            -o LeapYear
echo "Compiling LinearSearch1.c"
gcc -std=c11 LinearSearch1.c       -o LinearSearch1
echo "Compiling MaxAndMinValue.c"
gcc -std=c11 MaxAndMinValue.c      -o MaxAndMinValue
echo "Compiling MultiDimArray1.c"
gcc -std=c11 MultiDimArray1.c      -o MultiDimArray1
echo "Compiling NestedForLoop.c"
gcc -std=c11 NestedForLoop.c       -o NestedForLoop
echo "Compiling ReadEntireLine.c"
gcc -std=c11 ReadEntireLine.c      -o ReadEntireLine
echo "Compiling ReverseArray1.c"
gcc -std=c11 ReverseArray1.c       -o ReverseArray1
echo "Compiling Switch.c"
gcc -std=c11 Switch.c              -o Switch
echo "Compiling TestChars.c"
gcc -std=c11 TestChars.c           -o TestChars
echo "Compiling TokenizeString.c"
gcc -std=c11 TokenizeString.c      -o TokenizeString
echo "Compiling Transpose.c"
gcc -std=c11 Transpose.c           -o Transpose
echo "Compiling UpperLowerCount.c"
gcc -std=c11 UpperLowerCount.c     -o UpperLowerCount
echo "Compiling WhileLoop.c"
gcc -std=c11 WhileLoop.c           -o WhileLoop
echo "Compiling WhileLoopStr.c"
gcc -std=c11 WhileLoopStr.c        -o WhileLoopStr

echo ""
echo "Files containing strcpy:"
grep -l strcpy *.c

echo ""
echo "Files containing strncpy:"
grep -l strncpy *.c
