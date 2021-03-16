# => Calculate ROW averages for multiple files

#columns in rain.csv:
#DOW,inches of rain, degrees F, humidity (%)

#files: rain1.csv, rain2.csv, rain3.csv

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
' rain?.csv

