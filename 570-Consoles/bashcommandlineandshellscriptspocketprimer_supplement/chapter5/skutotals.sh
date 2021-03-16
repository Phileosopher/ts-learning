SKUVALUES="skuvalues.txt"
SKUSOLD="skusold.txt"

for sku in `cat $SKUVALUES`
do
  total=`cat $SKUSOLD |grep $sku | awk '{total += $2} END {print total}'`
  echo "UNITS SOLD FOR SKU $sku: $total"
done

