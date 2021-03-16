echo "05.20.144q.az.1.zip" | awk -F"." ' 
{
  f5=$5 + 1
  printf("%s.%s.%s.%s.%s.%s",$1,$2,$3,$4,f5,$6)
}'

