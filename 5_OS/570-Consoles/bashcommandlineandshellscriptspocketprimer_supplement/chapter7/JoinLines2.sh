cat columns2.txt | awk '
BEGIN { count = 0 }
{ 
   printf("%s",$0) 
   if( ++count % 2 == 0) { print " " }
}
'

