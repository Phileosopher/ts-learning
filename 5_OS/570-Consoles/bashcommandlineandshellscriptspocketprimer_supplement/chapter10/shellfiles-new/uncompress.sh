#!/bin/sh

zipfiles="`ls *zip`"

if [ "$zipfiles" != "" ]
then
  for f in `echo $zipfiles`
  do
    echo "Processing file: $f"
    f1=`echo $f | cut -d"." -f1`
    f2=`echo $f | cut -d"." -f2`
    newdir="${f1}-new"

    echo "Creating directory: $newdir"
    mkdir -p $newdir
    cp $f $newdir
    cd $newdir
    echo "Uncompressing file: $f"
    jar xvf $f
    cd ../
  done
else
  echo "No zip files found"
fi

