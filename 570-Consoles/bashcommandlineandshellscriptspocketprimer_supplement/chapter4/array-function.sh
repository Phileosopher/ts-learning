#!/bin/bash

# compact version of the code later in this script:
#items() { for line in "${@}" ; do printf "%s\n" "${line}" ; done ; }
#aa=( 7 -4 -e ) ; items "${aa[@]}"

items() {
  for line in "${@}"
  do  
    printf "%s\n" "${line}"
  done 
}

arr=( 123 -abc 'my data' )
items "${arr[@]}"

