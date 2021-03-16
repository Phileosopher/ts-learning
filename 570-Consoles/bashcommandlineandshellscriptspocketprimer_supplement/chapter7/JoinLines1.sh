cat columns2.txt | awk '
{ 
   printf("%s",$0) 
   if( $1 !~ /one/) { print " " }
}
'

