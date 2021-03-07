while (true)
do
  echo -n "Enter a string: "
  read var

  case ${var:0:1} in
  [0-9]*) echo "$var starts with a digit" ;;
  [A-Z]*) echo "$var starts with an uppercase letter" ;;
  [a-z]*) echo "$var starts with a lowercase letter" ;;
       *) echo "$var starts with another symbol" ;;
  esac
done

