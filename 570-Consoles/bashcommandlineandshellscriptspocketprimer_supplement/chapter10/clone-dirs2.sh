for d in `ls names`
do
  if [ -d $d ]
  then
    echo "Directory $d already exists" 
  else
    echo "Creating directory $d" 
    mkdir $d
  fi
done 

