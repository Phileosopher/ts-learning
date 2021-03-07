cat columns.txt | awk '
{ 
   if( NF == 2 ) { print $0 }
}
'

