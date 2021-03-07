infile="wordfile.txt"
outfile="converted.txt"
rm -f $outfile 2>/dev/null

while read line
do
  # word count of current line
  wordcount=`echo "$line" |wc -w`

  modvalue=`expr $wordcount % 2`
  if [ $modvalue = 0 ]
  then
    # even: convert to uppercase
    echo "$line" | tr '[a-z]' '[A-Z]' >> $outfile
  else
    # odd: convert to lowercase
    echo "$line" | tr '[A-Z]' '[a-z]' >> $outfile
  fi
done < $infile

