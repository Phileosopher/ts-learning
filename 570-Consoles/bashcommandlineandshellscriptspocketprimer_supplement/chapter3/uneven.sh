inputfile="uneven.txt"
outputfile="uneven.txt2"

# ==> four fields per line

#method #1: four fields per line 
cat $inputfile | xargs -n 4 >$outputfile

#method #2: two equal rows
#xargs -L 2 <$inputfile > $outputfile

#method #3: untested 
# paste -d' ' - - < $inputfile >$outputfile

echo "input file:"
cat $inputfile

echo "output file:"
cat $outputfile

