# The file is fed to the “tr” command, which changes uppercase to lowercase
# sed removes commas and periods, then changes whitespace to newlines
# uniq needs each word on its own line to count the words properly
# Uniq converts data to unique words and the number of times they appeared
# The final sort orders the data by the wordcount.

cat "$1" | xargs -n1 | tr A-Z a-z | \
sed -e 's/\.//g' -e 's/\,//g' -e 's/ /\ /g' | \
sort | uniq -c | sort -nr

