TOP=`pwd`

dirs="appendixa-keras appendixb-tf2 appendixc-pandas chapter1 chapter2 chapter3 chapter4 chapter5 chapter6"

for dir in `echo $dirs`
do
  cd $TOP/$dir
  for f in `ls *py`
  do
    echo "file: $f"
    python3 $f 
  done 
done
