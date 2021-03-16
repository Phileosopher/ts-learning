#!/bin/bash 

function checkNewUser() 
{
  echo "argument #1 = $1"
  echo "argument #2 = $2"
  echo "arg count   = $#"

  if test "$1" = "John" && test "$2" = "Smith" 
  then
    return 1
  else
    return 0
  fi
}

/bin/echo -n "First name: "
read fname
/bin/echo -n "Last name: "
read lname

checkNewUser $fname $lname 
echo "result = $?"

result=`checkNewUser $fname $lname`
echo "result = $result"
