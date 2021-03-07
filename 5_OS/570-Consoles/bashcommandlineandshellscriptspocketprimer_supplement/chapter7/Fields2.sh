
echo "a b c d e"| awk '
{ 
  for(i=1; i<=NF; i++) {
     print "Field ",i,":",$i
  }
}
'
