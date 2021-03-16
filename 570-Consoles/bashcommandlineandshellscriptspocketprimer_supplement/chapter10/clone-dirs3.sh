for d in `ls names`
do
  if [ -f $d ]
  then
    echo "$d is a file (not a directory)" 
  elif [ -d $d ]
  then
    echo "Directory $d already exists" 
  else
    echo "Creating directory $d" 
    mkdir $d
  fi
done 

