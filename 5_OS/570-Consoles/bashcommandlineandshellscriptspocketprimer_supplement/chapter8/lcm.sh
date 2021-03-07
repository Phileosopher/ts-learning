#!/bin/sh

function gcd()
{
  if [ $1 -lt $2 ]
  then
    result=`gcd $2 $1`
    echo $result 
  else
    remainder=`expr $1 % $2`

    if [ $remainder == 0 ]
    then
      echo $2 
    else 
      result=`gcd $2 $remainder`
      echo $result
    fi
  fi
}

function lcm()
{
   gcd1=`gcd $1 $2`
   lcm1=`expr $1 / $gcd1` 
   lcm2=`expr $lcm1 \* $2` 
   echo $lcm2
}

a="24"
b="10"
result=`lcm $a  $b`
echo "The LCM of $a and $b = $result"

a="10"
b="30"
result=`lcm $a  $b`
echo "The LCM of $a and $b = $result"

