#!/bin/bash

inputfile="namepairs.csv"
outputfile="reversenames.csv"
fnames="fnames"
lnames="lnames"

cat $inputfile|cut -d"," -f1 > $fnames
cat $inputfile|cut -d"," -f2 > $lnames

#NOTE: the following command only works 
#from the command line but NOT here:
paste –d',' $lnames $fnames > $outputfile
