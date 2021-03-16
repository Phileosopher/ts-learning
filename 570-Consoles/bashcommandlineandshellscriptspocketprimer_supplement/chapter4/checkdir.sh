# initialize 'counter' variables
TOTAL_FILES=0
ASCII_FILES=0
NONASCII_FILES=0
READABLE_FILES=0
EXEC_FILES=0
DIRECTORIES=0

for f in `ls`
do
  TOTAL_FILES=`expr $TOTAL_FILES + 1`

  if [ -d $f ]
  then
    DIRECTORIES=`expr $DIRECTORIES + 1`
  fi 

  if [ -x $f ]
  then
    EXEC_FILES=`expr $EXEC_FILES + 1`
  fi 

  if [ -r $f ]
  then
    READABLE_FILES=`expr $READABLE_FILES + 1`
  fi 

  readable=`file $f`
  ascii=`echo $readable |grep ASCII`
  if [ "$ascii" != "" ]
  then
    ASCII_FILES=`expr $ASCII_FILES + 1`
  else 
    #echo "readable: $readable"
    NONASCII_FILES=`expr $NONASCII_FILES + 1`
  fi 
done

# results:
echo "TOTAL_FILES:     $TOTAL_FILES"
echo "DIRECTORIES:     $DIRECTORIES"
echo "EXEC_FILES:      $EXEC_FILES"
echo "ASCII_FILES:     $ASCII_FILES"
echo "NON-ASCII_FILES: $NONASCII_FILES"

