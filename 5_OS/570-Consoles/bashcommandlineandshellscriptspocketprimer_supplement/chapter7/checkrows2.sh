
files="`ls data*.csv| tr '\n' ' '`"
echo "List of files: $files"

awk -F"," '
( FNR==2 || FNR==5 || FNR==7 ) {
    if ( $3 == "past" ) { count++ } 
}
END {
    printf "past: matched %d times (EXACT) ", count
    printf "in field 3 in lines 2/5/7\n"
}' data*.csv

#-----------------------
# Note: change $3 ~ "past" into $3 == "past" if you want an exact match (instead of a grep, as you did use in your own example, so that it also matches: somethingP2otherthing and variants thereof)

# FNR = File's Number of Records = number of lines into the current file (ie, starts again at 1 at each file's first line) (Current file whose name can also be known by the internal variable: FILENAME)

# (NR = here would not work, as it is the (total) Number or Records read since the beginning (not since the beginning of the current file) )
#-----------------------

