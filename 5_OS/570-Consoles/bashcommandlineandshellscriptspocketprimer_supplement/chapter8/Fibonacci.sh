#!/bin/sh

LOGFILE="/tmp/a1"
rm -f $LOGFILE 2>/dev/null

fib()
{
   if [ "$1" -gt 3 ] 
   then
echo "1 = $1 2 = $2 3 = $3" >> $LOGFILE 

      decr1=`expr $2 - 1`
      decr2=`expr $3 - 1`
      decr3=`expr $3 - 2`
echo "d1 = $decr1 d2 = $decr2 d3 = $decr3" >> $LOGFILE 

      fib1=`fib $2 $3 $decr2`
      fib2=`fib $3 $decr2 $decr3`
      fib=`expr $fib1 + $fib2`
      echo $fib 
   else
      if [ "$1" -eq 3 ]
      then
        echo 2
      else 
        echo 1
      fi
   fi
}

echo "Enter a number: "
read num

# add code to ensure it's a positive integer

if [ "$num" -lt 3 ]
then
  echo "fibonacci $num = 1"
else
  decr1=`expr $num - 1`
  decr2=`expr $num - 2`
  echo "fibonacci $num = `fib $num $decr1 $decr2`"
fi 

