#!/bin/bash

# method #1:
fruits[0]="apple" 
fruits[1]="banana" 
fruits[2]="cherry"
fruits[3]="orange" 
fruits[4]="pear"
echo "first fruit: ${fruits[0]}"
  
# method #2:
declare -a fruits2=(apple banana cherry orange pear)
echo "first fruit: ${fruits2[0]}"

# range of elements:
echo "last two: ${fruits[@]:3:2}"

# substring of element:
echo "substring: ${fruits[1]:0:3}"

arrlength=${#fruits[@]}
echo "length: ${#fruits[@]}"

