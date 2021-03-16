x=0
x=`expr $x + 1`
echo "new x: $x"

while (true)
do
  echo "x = $x"
  x=`expr $x + 1`
  if [ $x -gt 4 ]
  then
    break
  fi
done

