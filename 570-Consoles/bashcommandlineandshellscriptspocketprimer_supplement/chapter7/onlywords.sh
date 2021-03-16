x="ghi abc Ghi 123 #def5 123z"

echo "Only words:"
echo $x |tr -s ' ' '\n' | awk -F" " ' 
{
  if($0 ~ /^[a-zA-Z]+$/) { print $0 } 
}
' | sort | uniq
echo 

echo "Only integers:"
echo $x |tr -s ' ' '\n' | awk -F" " ' 
{
  if($0 ~ /^[0-9]+$/) { print $0 } 
}
' | sort | uniq
echo 

echo "Only alphanumeric words:"
echo $x |tr -s ' ' '\n' | awk -F" " ' 
{
  if($0 ~ /^[0-9a-zA-Z]+$/) { print $0 } 
}
' | sort | uniq
echo 

