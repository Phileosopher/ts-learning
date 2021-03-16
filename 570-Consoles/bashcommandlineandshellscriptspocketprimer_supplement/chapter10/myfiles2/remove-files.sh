# keep track of the top directory 
topdir=`pwd`

for f in `ls`
do
  if [ -d $f ]
  then
    cd $topdir/$f

    if [ -f "remove.sh" ]
    then
      echo "executing remove.sh in $f"
      sh remove.sh
    else
      echo "cannot find remove.sh in $f"
    fi

    cd $topdir
  fi 
done

