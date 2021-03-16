#!/bin/sh

function divisors()
{
   div="2"
   num="$1"
   primes=""

   while (true)
   do
     remainder=`expr $num % $div`

     if [ $remainder == 0 ]
     then
      #echo "divisor: $div"
       primes="${primes} $div"
       num=`expr $num / $div`
     else
       div=`expr $div + 1`
     fi

     if [ $num -eq  1 ]
     then 
       break 
     fi
   done 

   # use 'echo' instead of 'return'
   echo $primes
}

num="12"
primes=`divisors $num`
echo "The prime divisors of $num: $primes" 

num="768"
primes=`divisors $num`
echo "The prime divisors of $num: $primes" 

#num="12345"
#primes=`divisors $num`
#echo "The prime divisors of $num: $primes" 

#num="23768"
#primes=`divisors $num`
#echo "The prime divisors of $num: $primes" 

