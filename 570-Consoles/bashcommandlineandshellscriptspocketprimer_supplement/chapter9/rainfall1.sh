# => Calculate COLUMN averages for multiple files

#columns in rain.csv:
#DOW,inches of rain, degrees F, humidity (%)

#files: rain1.csv, rain2.csv, rain3.csv
echo "FILENAMES:"
ls rain?.csv

awk -F',' '
{
  inches+=$2
  degrees+=$3
  humidity+=$4
}
END {
  printf("FILENAME: %s\n", FILENAME)
  printf("inches:   %.2f\n", inches/7)
  printf("degrees:  %.2f\n", degrees/7)
  printf("humidity: %.2f\n", humidity/7)
}
' rain?.csv

