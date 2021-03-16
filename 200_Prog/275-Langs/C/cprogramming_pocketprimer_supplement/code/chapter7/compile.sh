echo "Compiling ArrayOfEmployees.c"
gcc -std=c11 ArrayOfEmployees.c -o ArrayOfEmployees
echo "Compiling BitOperations.c"
gcc -std=c11 BitOperations.c    -o BitOperations
echo "Compiling Bitfields.c"
gcc -std=c11 Bitfields.c        -o Bitfields
echo "Compiling BubbleSort1.c"
gcc -std=c11 BubbleSort1.c      -o BubbleSort1
echo "Compiling DateTimeString.c"
gcc -std=c11 DateTimeString.c   -o DateTimeString
echo "Compiling DivByZero.c"
gcc -std=c11 DivByZero.c        -o DivByZero
echo "Compiling DontDoThis.c"
gcc -std=c11 DontDoThis.c       -o DontDoThis
echo "Compiling EmployeeStruct1.c"
gcc -std=c11 EmployeeStruct1.c  -o EmployeeStruct1
echo "Compiling EmployeeStructs.c"
gcc -std=c11 EmployeeStructs.c  -o EmployeeStructs
# do not change the order of the next two lines:
echo "Compiling FindMain2.c"
gcc -std=c11 -Wall              -c FindChar2.c
gcc -std=c11 FindChar2.o FindMain2.c -o FindMain2 
echo "Compiling NestedStructures.c"
gcc -std=c11 NestedStructures.c -o NestedStructures
echo "Compiling PrintEnvVars.c"
gcc -std=c11 PrintEnvVars.c     -o PrintEnvVars
echo "Compiling SLinkedList.c"
gcc -std=c11 SLinkedList.c      -o SLinkedList
echo "Compiling SetEnvVars.c"
gcc -std=c11 SetEnvVars.c       -o SetEnvVars
echo "Compiling ShowBits.c"
gcc -std=c11 ShowBits.c         -o ShowBits
echo "Compiling SimpleMacro.c"
gcc -std=c11 SimpleMacro.c      -o SimpleMacro
echo "Compiling SystemDeleteFile.c"
gcc -std=c11 SystemDeleteFile.c -o SystemDeleteFile
echo "Compiling SystemForkExec.c"
gcc -std=c11 SystemForkExec.c   -o SystemForkExec
echo "Compiling Unions.c"
gcc -std=c11 Unions.c           -o Unions
echo "Compiling Vector.c"
gcc -std=c11 Vector.c           -o Vector

echo ""
echo "Files containing strcpy:"
grep -l strcpy *.c

echo ""
echo "Files containing strncpy:"
grep -l strncpy *.c

