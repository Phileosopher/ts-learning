
inputfile="multiple-delims2.dat"
cat $inputfile | sed -e 's/:/,/' -e 's/|/,/' -e 's/\^/,/g'

