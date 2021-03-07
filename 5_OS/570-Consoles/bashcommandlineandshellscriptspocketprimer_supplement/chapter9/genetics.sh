# required output:
#xyz3:77774:XYZ123
#xyz3:84362:WASH7P

awk -F" " '
{
  if( $3 == "gene" ) {
    split($6, triplet, /[;=]/)
    printf("%s:%s:%s\n", $1, $4, triplet[2] )
  }
}
' genetics.txt

