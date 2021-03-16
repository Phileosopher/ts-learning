if [ -d textfiles ]
then
  rm -r textfiles
fi

mkdir textfiles
cp `ls *txt` textfiles

