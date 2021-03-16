DataFile="mylogfile.txt"
OK="okay"
ERROR="error"
sleeptime="2"
loopcount=0

rm -f $DataFile 2>/dev/null; touch $DataFile
newline="`date` SYSTEM IS OKAY"
echo $newline >> $DataFile

while (true)
do
  loopcount=`expr $loopcount + 1`
  echo "sleeping $sleeptime seconds..."
  sleep $sleeptime
  echo "awake again..."

  lastline=`tail -1 $DataFile`

  if [ "$lastline" == "" ]
  then
    continue
  fi

  okstatus=`echo $lastline |grep -i $OK`
  badstatus=`echo $lastline |grep -i $ERROR`

  if [ "$okstatus" != "" ]
  then
    echo "system is normal"

    if (( $loopcount > 5 ))
    then
       newline="`date` SYSTEM IS OKAY"
    else
       newline="`date` SYSTEM ERROR"
    fi
    echo $newline >> $DataFile
  elif [ "$badstatus" != "" ]
  then
    echo "Error in logfile: $lastline"
    break
  fi
done

