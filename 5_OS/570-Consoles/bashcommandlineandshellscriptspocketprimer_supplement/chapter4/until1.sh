x="0"
until [ "$x" = "5" ]
do
  x=`expr $x + 1`
  echo "x: $x"
done

