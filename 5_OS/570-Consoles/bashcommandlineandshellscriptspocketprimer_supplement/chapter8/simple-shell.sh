#!/bin/sh

function1 ()
{
   echo "inside function 1" 
}

function2 ()
{
   echo "you entered $1 in function 2" 
}

# invoke function1 here:
function1

echo "Enter a string: "
read str

# invoke function2 here:
function2 str

