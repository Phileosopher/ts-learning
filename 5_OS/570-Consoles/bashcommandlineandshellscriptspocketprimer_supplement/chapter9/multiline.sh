# Records are separated by blank lines
awk ' 
BEGIN { RS = "" ; FS = "\n" }
{
   gsub(/[ \t]+$/, "", $1) 
   gsub(/[ \t]+$/, "", $2) 
   gsub(/[ \t]+$/, "", $3) 

   gsub(/^[ \t]+/, "", $1) 
   gsub(/^[ \t]+/, "", $2) 
   gsub(/^[ \t]+/, "", $3) 

   print $1 ":" $2 ":" $3 ""
  #printf("%s:%s:%s\n",$1,$2,$3) 
}
' multiline.txt 
