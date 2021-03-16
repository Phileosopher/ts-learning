inputfile="transact1.csv"
rfile="recordtransact1.csv"
pfile="pendingtransact1.csv"

grep "^record"  $inputfile | sed 's/cash_//g; s/day_//g' > $rfile
grep "^pending" $inputfile | sed 's/cash_//g; s/day_//g' > $pfile

cat $rfile
echo "======"
cat $pfile
