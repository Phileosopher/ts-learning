#!/bin/bash
# http://www.thegeekstuff.com/2010/06/bash-array-tutorial 

fruits[0]="apple" 
fruits[1]="banana" 
fruits[2]="cherry" 
fruits[3]="orange" 
fruits[4]="pear"

# array length:
arrlength=${#fruits[@]}
echo "length: ${#fruits[@]}"

# print each element via a loop:
for (( i=1; i<${arrlength}+1; i++ ));
do
  echo "element $i of ${arrlength} : " ${fruits[$i-1]}
done

