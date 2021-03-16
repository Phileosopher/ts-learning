
key="2000" 
if [ "`grep $key mykeys.txt`" != "" ]
then
 foundkey=true
else
  foundkey=false
fi

linecount="`grep $key mykeys.txt |wc -l |tr -d ' '`"
linecount2="`grep $key mykeys.txt |wc -l |tr -s ' '`"

echo "current key = $key"
echo "found key   = $foundkey"
echo "linecount   = $linecount"
echo "linecount2  = $linecount2"

