#!/bin/sh

iterate() 
{ 
   echo "Argument count: $#"
   echo "Argument list:  $@"
   echo ""

   for i in "${@}" 
   do
     echo "argument: $i"
   done
}

iterate a "b c" d "e f"

