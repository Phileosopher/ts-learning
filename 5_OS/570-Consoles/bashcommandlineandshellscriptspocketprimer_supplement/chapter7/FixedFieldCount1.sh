
echo "aa bb cc dd ee ff gg hh"| awk '
BEGIN { colCount = 3 } 
{ 
  for(i=1; i<=NF; i++) {
     printf("%s ", $i)
     if(i % colCount == 0) {
        print " "
     }
  }
}
'

