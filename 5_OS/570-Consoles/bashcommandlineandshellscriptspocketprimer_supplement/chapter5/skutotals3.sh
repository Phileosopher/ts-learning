SKUVALUES="skuvalues.txt"
SKUSOLD="skusold.txt"
TOTALS="totalspersku.txt"
rm -f $TOTALS 2>/dev/null 

##############################
#calculate totals for each sku 
##############################
for sku in `cat $SKUVALUES`
do
  total=`cat $SKUSOLD |grep $sku | awk '{total += $2} END {print total}'`
  echo "UNITS SOLD FOR SKU $sku: $total"
  echo "$sku|$total" >> $TOTALS
done

##########################
#calculate max/min/average
##########################
cat $TOTALS | awk -F"|" '
  BEGIN {first = 1;} 
  {if(first) { min = max= avg = sum = $2; first=0; next}}
  { if($2 < min) { min = $2 }
    if($2 > max) { max = $2 }
    sum += $2
  } 
  END {print "Minimum = ",min
       print "Maximum = ",max
       print "Average = ",avg
       print "Total   = ",sum
  }
'

