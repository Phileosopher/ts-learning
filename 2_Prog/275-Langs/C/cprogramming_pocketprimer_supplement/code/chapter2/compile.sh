echo "Compiling AngleSum.c" 
gcc -std=c11 AngleSum.c -o              AngleSum
echo "Compiling Array100.c" 
gcc -std=c11 Array100.c -o              Array100
echo "Compiling CharArray.c" 
gcc -std=c11 CharArray.c -o             CharArray
echo "Compiling CopyFunction.c" 
gcc -std=c11 CopyFunction.c -o          CopyFunction
echo "Compiling CopyString.c" 
gcc -std=c11 CopyString.c -o            CopyString
echo "Compiling FirstLastName.c" 
gcc -std=c11 FirstLastName.c -o         FirstLastName
echo "Compiling SimpleAdder.c"    
gcc -std=c11 SimpleAdder.c -o           SimpleAdder
echo "Compiling IfElse.c" 
gcc -std=c11 IfElse.c -o                IfElse
echo "Compiling IfElse2.c" 
gcc -std=c11 IfElse2.c -o               IfElse2
echo "Compiling IfElse3.c" 
gcc -std=c11 IfElse3.c -o               IfElse3
echo "Compiling IfElse4.c" 
gcc -std=c11 IfElse4.c -o               IfElse4
echo "Compiling LocalVars.c" 
gcc -std=c11 LocalVars.c -o             LocalVars
echo "Compiling MaxAndMin.c" 
gcc -std=c11 MaxAndMin.c -o             MaxAndMin
echo "Compiling OrderedValues.c" 
gcc -std=c11 OrderedValues.c -o         OrderedValues
echo "Compiling PrintfSamples.c" 
gcc -std=c11 PrintfSamples.c -o         PrintfSamples
echo "Compiling PromoteVar.c" 
gcc -std=c11 PromoteVar.c -o            PromoteVar
echo "Compiling ReadFormattedLine.c" 
gcc -std=c11 ReadFormattedLine.c -o     ReadFormattedLine
echo "Compiling ReadLine.c" 
gcc -std=c11 ReadLine.c -o              ReadLine
echo "Compiling ReadSingleChar.c" 
gcc -std=c11 ReadSingleChar.c -o        ReadSingleChar
echo "Compiling Strpcp1.c" 
gcc -std=c11 Strcpy1.c -o               Strcpy1
echo "Compiling TypeCast.c" 
gcc -std=c11 TypeCast.c -o              TypeCast

echo ""
echo "Files containing strcpy:"
grep -l strcpy *.c

echo ""
echo "Files containing strncpy:"
grep -l strncpy *.c

