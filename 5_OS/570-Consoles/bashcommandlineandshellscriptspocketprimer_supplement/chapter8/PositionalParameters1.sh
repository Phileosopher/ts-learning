echo "number of arguments: $#"
echo "command name: $0"
echo "all params: $1 $2 $3 $4 $5 $6 $7 $8 $9"
echo "all params: $*"
echo "all params: $@"
echo "exit status: $?"
echo "process id: $$"

if [ x"$1" != "x" ]
then
  echo "Position parameter #1 = $1"
else
  echo "Position parameter #1 is null"
fi

if [ "$5" == "" ]
then
  echo "Position parameter #5 is nul1"
fi

case $1 in
  n|N) echo "#1 is an n or N" ;;
  y*|Y*) echo "#1 starts with a y or Y" ;;
  *) echo "no matches occurred" ;;
esac

