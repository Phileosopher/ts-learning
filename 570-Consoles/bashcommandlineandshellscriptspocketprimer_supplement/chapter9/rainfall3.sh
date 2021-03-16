# => Calculate COLUMN averages for multiple files (backtick)

#columns in rain.csv:
#DOW,inches of rain, degrees F, humidity (%)

# specify the list of CSV files (supports multiple regexs)
files=`ls rain*csv zain*csv`

echo "FILES: `echo $files`"
  
awk -F',' '
{ 
  mon_rain[FNR]+=$2
  mon_degrees[FNR]+=$3
  mon_humidity[FNR]+=$4
  idx[FNR]++
} 
END {
  printf("DAY INCHES DEGREES HUMIDITY\n")
     
  for(i=1; i<=FNR; i++){
    printf("%3d %-6.2f %-8.2f %-7.2f\n",
     i,mon_rain[i]/idx[i],mon_degrees[i]/idx[i],mon_humidity[i]/idx[i])
  }
}
' `echo $files`

