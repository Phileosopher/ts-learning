mylib2="mylib2.a"

for f in `ls *.o`
do
  echo "Adding object file $f"
  ar r $mylib2 $f
done

