
function divisors()
{
   div="2"
   num="$1"

   while (true)
   do
     remainder=`expr $num % $div`

     if [ $remainder == 0 ]
     then
       echo "divisor: $div"
       num=`expr $num / $div`
     else
       div=`expr $div + 1`
     fi

     if [ $num -eq  1 ]
     then 
       break
     fi
   done 
}

n="12"
echo "The divisors of $n:" 
divisors $n

