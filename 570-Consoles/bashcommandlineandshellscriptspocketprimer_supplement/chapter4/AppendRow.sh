DataFile="users.txt"

addUser()
{
  echo -n "First Name: "
  read fname

  echo -n "Last Name: "
  read lname

  if [ -n $fname -a -n $lname ]
  then
    # append new line to the file
    echo "$fname $lname" >> $DataFile
  else
    echo "Please enter non-empty values"
  fi
}

while (true)
do
  echo ""
  echo "List of Users"
  echo "============="
  cat users.txt 2>/dev/null

  echo "-----------------------------"
  echo "Enter 'a' to add a new user"
  echo "Enter 'd' to delete all users"
  echo "Enter 'x' to exit this menu"
  echo "-----------------------------"
  echo

  read answer
  case $answer in
    a|A) addUser ;; 
    d|D) rm $DataFile 2>/dev/null ;;
    x|X) break ;; 
  esac
done

