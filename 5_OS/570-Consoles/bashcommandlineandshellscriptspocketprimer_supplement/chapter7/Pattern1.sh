cat columns2.txt | awk ' 
   /^f/    { print $1 }
   /two $/ { print $1 }
'

