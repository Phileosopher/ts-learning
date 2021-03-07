# make sure that you "cd" into the "names2" directory

echo "hello world" >/tmp/file1
file1="/tmp/file1"

for d in `ls`
do
  if [ -f $d ]
  then
    echo "Skipping copy command for $d"
  elif [ -d $d ]
  then
    echo "Copying $file1 into $d"
    cp $file1 $d
  else
    echo "Creating directory $d" 
    mkdir $d
    echo "Copying $file1 into $d"
    cp $file1 $d
  fi
done 

