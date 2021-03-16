#!/bin/sh

maxCount="10"

screenchange()
{
   echo "Caught a signal based on the trap statement."
}

echo "Resize the current command shell."
trap screenchange SIGWINCH

COUNT=0
while [ $COUNT -lt $maxCount ] ; do
  COUNT=$(($COUNT + 1))
  sleep 1
done

