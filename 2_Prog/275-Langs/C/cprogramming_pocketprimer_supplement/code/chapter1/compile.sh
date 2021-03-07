echo "Compiling AbsValues.c"
gcc -std=c11 AbsValues.c  -o      AbsValues
echo "Compiling AddArray.c"
gcc -std=c11 AddArray.c -o        AddArray
echo "Compiling Arithmetic.c"
gcc -std=c11 Arithmetic.c -o      Arithmetic
echo "Compiling HelloWorld.c"
gcc -std=c11 HelloWorld.c -o      HelloWorld
echo "Compiling IntExample.c"
gcc -std=c11 IntExample.c -o      IntExample
echo "Compiling MathValues.c"
gcc -std=c11 MathValues.c -o      MathValues
echo "Compiling OtherBases.c"
gcc -std=c11 OtherBases.c -o      OtherBases
echo "Compiling ReverseChars.c"
gcc -std=c11 ReverseChars.c -o    ReverseChars
echo "Compiling SizeOfDataTypes.c"
gcc -std=c11 SizeOfDataTypes.c -o SizeOfDataTypes
echo "Compiling TrigValues.c"
gcc -std=c11 TrigValues.c -o      TrigValues

echo ""
echo "Files containing strcpy:"
grep -l strcpy *.c

echo ""
echo "Files containing strncpy:"
grep -l strncpy *.c
