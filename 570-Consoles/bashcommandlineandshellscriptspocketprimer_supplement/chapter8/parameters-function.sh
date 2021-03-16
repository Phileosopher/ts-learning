#!/bin/sh

function1 ()
{
   echo "top of function 1" 
   echo "param 1: $1"
   echo "param 2: $2"
   echo "param 3: $3"
}

# invoke function1 here:
function1 a 
function1 a b
function1 a b c

