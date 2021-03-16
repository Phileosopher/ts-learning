while (true)
do
  echo -n "Enter a string: "
  read var

  case ${var:0:2} in
  [0-9][0-9]) echo "$var starts with to digit" ;;
  [A-Z][A-Z]) echo "$var starts with two uppercase letters" ;;
  [a-z][a-z]) echo "$var starts with two lowercase letters" ;;
       *) echo "$var starts with another pattern" ;;
  esac
done

