#!/bin/bash
numbers="1 2 3 4 5 6 7 8 9 10"
array1=( `echo "$numbers" `)
total1=0
total2=0

for num in "${array1[@]}"
do
 #echo "array item: $num"
  total1+=$num
  let total2+=$num
done

echo "Total1: $total1"
echo "Total2: $total2"

