awk '{ for(i=1; i<=NF;i++) j+=$i; print j; j=0 }' numbers.txt

