x="abc"

if [ -z "$y" ]
then
  y="def"
  echo "y is defined: $y"
else
  echo "y is defined: $y"
fi

