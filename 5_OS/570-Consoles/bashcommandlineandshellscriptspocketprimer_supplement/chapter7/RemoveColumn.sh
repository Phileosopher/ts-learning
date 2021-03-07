awk '{ for (i=2; i<=NF; i++) printf "%s ", $i; printf "\n"; }' products.txt
