# => combinations of columns
awk -F',' '
{
  $2 += $3 * 2 + $4 / 2
  $3 += $4 / 3 + $2 * $2 / 10
  $4 += $2 + $3
  $1 += $2 * 3 - $4 / 10
  printf("%d,%.2f,%.2f,%.2f\n",$1,$2,$3,$4)
} 
' rain?.csv

