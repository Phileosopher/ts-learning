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
      echo `gcd $2 $remainder`
    fi
  fi
}

a="4"
b="20"
result=`gcd $a $b`
echo "GCD of $a and $b = $result"

a="4"
b="22"
result=`gcd $a $b`
echo "GCD of $b and $a = $result"

a="20"
b="3"
result=`gcd $a $b`
echo "GCD of $b and $a = $result"

a="10"
b="10"
result=`gcd $a $b`
echo "GCD of $b and $a = $result"

