foundlist=""
notfoundlist=""

if [ "$#" == 0 ]
then
   echo "Usage: $0 <string-list>"
   exit
fi

zipfiles=`ls *zip 2>/dev/null`

if [ "$zipfiles" = "" ]
then
   echo "*** No zip files in `pwd` ***"
   exit
fi

for str in "$@"
do
  echo "Checking zip files for $str:"
  for f in `ls *zip`
  do
    found=`unzip -v $f |grep "$str"`
    if [ "$found" != "" ]
    then
      foundlist="$f ${foundlist}"
    else
      notfoundlist="$f ${notfoundlist}"
    fi
  done

  echo "Files containing $str:"
  echo $foundlist| tr ' ' '\n'

  echo "Files not containing $str:"
  echo $notfoundlist |tr ' ' '\n'
  foundlist=""
  notfoundlist=""
done

