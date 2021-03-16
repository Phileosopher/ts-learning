# NF is the number of fields in the current record.
# NR is the number of the current record/line 
# (not the number of records in the file).
# In the END block (or the last line of the file) 
# it's the number of lines in the file.
# Solution in R: https://gist.github.com/dsparks/3693115

echo "Main diagonal:"
awk -F"," '{ for (i=0; i<=NF; i++) if (NR >= 1 && NR == i) print $(i) }' diagonal.csv

echo "Off diagonal:"
awk -F"," '{print $(NF+1-NR)}' diagonal.csv 

echo "Main diagonal sum:"
awk -F"," ' 
BEGIN { sum = 0 } 
{
  for (i=0; i<=NF; i++) { if (NR >= 1 && NR == i) { sum += $i } }
}
END { printf ("sum = %s\n",sum) } 
' diagonal.csv
echo "Off diagonal sum:"
awk -F"," '
BEGIN { sum = 0 }
{
  for (i=0; i<=NF; i++) { if(NR >= 1 && i+NR == NF+1) { sum += $i; } }
}
END { printf ("sum = %s\n",sum) }
' diagonal.csv

