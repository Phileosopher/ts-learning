menu()
{
  echo "1) Perform system backup"
  echo "2) Read tape drive"
  echo "x) Exit System"
  echo ""
  echo "Enter option:"
}

process_option()
{
  case $option in 
    1) echo "Starting system backup...";;
    2) echo "Reading tape drive...";;
    x) echo "Are you really sure? (Y/n)"
       read val
       val=$val | tr '[:upper:]' '[:lower:]'

       if [ "$val" = "y" ]
       then 
         echo "Exiting system ... goodbye" 
         exit 
       fi ;; 
    *) echo "Exiting system ... goodbye" 
       exit ;;
  esac
}

while(true) 
do
  menu
  read option
  process_option
done

