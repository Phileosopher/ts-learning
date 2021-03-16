SKUVALUES="skuvalues.txt"
SKUSOLD="skusold.txt"
SKUPRICES="skuprices.txt"

for sku in `cat $SKUVALUES`
do
  skuprice=`grep $sku $SKUPRICES | cut -d" " -f2`
  subtotal=`cat $SKUSOLD |grep $sku | awk '{total += $2} END {print total}'`
  total=`echo "$subtotal * $skuprice" |bc`
  echo "AMOUNT SOLD FOR SKU $sku: $total"
done

