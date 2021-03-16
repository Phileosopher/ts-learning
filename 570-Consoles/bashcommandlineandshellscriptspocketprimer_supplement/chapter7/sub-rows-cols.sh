#-----------------------------------------
# 1) remove blank lines
# 2) remove line feeds
# 3) print a LF after every fourth field
# 4) remove trailing ',' from each row 
#-----------------------------------------
inputfile="mixed-data.csv"
outputfile="sub-rows-cols.csv"

grep -v "^$" $inputfile |awk -F"," '{printf("%s",$0)}' | awk '
BEGIN { columnCount = 4 }
{
   for(i=1; i<=NF; i++) {
     printf("%s ", $i) 
     if( i % columnCount  == 0) { print "" }
   } 
}' > temp-columns 

# 4) remove trailing ',' from output:
cat temp-columns | sed 's/, $//' | sed 's/ $//' > temp-columns2

cat temp-columns2 | awk '
BEGIN { rowCount = 2; currRow = 0 }
{ 
   if(currRow % rowCount == 0) { print $1, $3 }
   ++currRow 
}' > temp-columns3 

cat temp-columns3 | sed 's/,$//' | sed 's/ $//' > $outputfile

