inputfile="linepairs.csv"
outputfile="linepairsjoined.csv"

# join pairs of consecutive lines:
paste -d " "  - - < $inputfile > $outputfile

# join three consecutive lines:
#paste -d " "  - - - < $inputfile > $outputfile

# join four consecutive lines:
#paste -d " "  - - - - < $inputfile > $outputfile

