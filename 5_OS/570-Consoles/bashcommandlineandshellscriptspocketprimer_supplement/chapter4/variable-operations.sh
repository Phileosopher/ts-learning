#length of myvar: 
myvar=123456789101112
echo ${#myvar}

#print last 5 characters of myvar:
echo ${myvar: -5} 

#10 if myvar was not assigned 
echo ${myvar:-10}  

#last 10 symbols of myvar
echo ${myvar: -10} 

#substitute part of string with echo: 
echo ${myvar//123/999}

#add integers a to b and assign to c:
a=5
b=7
c=$((a+b))
echo "a: $a b: $b c: $c"
#error:
#c=`expr $a + $b`
#error:
#c=`echo "$a+$b"|bc`

