while(true)
do
  echo -n "Proceed with backup (Y/y/N/n): "
  read response

  case $response in
    n*|N*) proceed="false" ;;
    y*|Y*) proceed="true"  ;;
    *) proceed="unknown"   ;;
  esac

  if [ "$proceed" = "true" ]
  then
    echo "proceeding with backup"
    break
  elif [ "$proceed" = "false" ]
  then
    echo "cancelling backup"
  else
    echo "Invalid response"
  fi
done

