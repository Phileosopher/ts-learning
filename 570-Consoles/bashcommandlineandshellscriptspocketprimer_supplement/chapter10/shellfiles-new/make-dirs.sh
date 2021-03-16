###################################################
# Define a variable with a list of directory names
# This method does not depend on an external file.
# Alternatively, place these names in a text file
# and then read the contents of that text file.
###################################################

# change the value of mydir to whatever you need
mydir="names"

name_list="andrew-webber dave-jones jane-smith john-smith keith-thompson"

if [ ! -d $mydir ]
then
  mkdir $mydir
  cd $mydir

  for name in `echo $name_list`
  do
    echo "creating directory $name in $mydir"
    mkdir $name
  done
else
  echo "Directory $mydir exists"
fi
