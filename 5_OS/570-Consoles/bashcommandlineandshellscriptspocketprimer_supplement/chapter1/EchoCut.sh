x1="123   456   789"
x2="123 456 789"
echo "x1 = $x1"
echo "x2 = $x2"
 
x3=`echo $x1   | cut -c1-7`
x4=`echo "$x1" | cut -c1-7`
x5=`echo $x2   | cut -c1-7`
echo "x3 = $x3"
echo "x4 = $x4"
echo "x5 = $x5"

