#!/bin/sh

iterate()
{
  echo "this will be skipped ... why?"
}

iterate() 
{ 
   arg1="$1"; shift; 
   for arg 
   do 
     echo "value: $arg"; 
   done
}

iterate a b c d e

