#!/bin/bash

factorial()
{
   num=$1
   result=1
   for (( i=2; i<=${num}; i++ ));
   do
     result=$((${result}*$i))
   done

   echo $result
}

printf "Enter a number: "
read num

echo "$num! = `factorial $num`"

