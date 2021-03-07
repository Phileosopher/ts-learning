
cat digits.txt |awk -F" " '{
  printf("%d",$0)
  if(NR % 3 == 0) { printf("\n") } 
}'

