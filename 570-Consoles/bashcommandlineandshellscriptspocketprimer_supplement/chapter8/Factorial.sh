#!/bin/sh

factorial()
{
   if [ "$1" -gt 1 ] 
   then
      decr=`expr $1 - 1`
      result=`factorial $decr`
      product=`expr $1 \* $result`
      echo $product
   else
      # we have reached 1:
      echo 1
   fi
}

echo "Enter a number: "
read num

# add code to ensure it's a positive integer

echo "$num! = `factorial $num`"

