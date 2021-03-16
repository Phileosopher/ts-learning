#!/bin/bash

names="names.txt"
contents1=( `cat "$names"` )

echo "First loop:"
for w in "${contents1[@]}"
do
  echo "$w"
done

IFS=""
names="names.txt"
contents1=( `cat "$names"` )

echo "Second loop:"
for w in "${contents1[@]}"
do
  echo "$w"
done

