# initialize variables for the three main files
MasterOrders="MasterOrders.txt"
CustomerDetails="Customers.txt"
PurchaseOrders="PurchaseOrders.txt"

# iterate through the "master table"
for mastCustId in `cat $MasterOrders | cut -d" " -f2`
do
  # get the customer information
  custDetails=`grep $mastCustId $CustomerDetails`

  # get the id from the previous line
  custDetailsId=`echo $custDetails | cut -d" " -f1`

  # get the customer PO from the PO file
  custPO=`grep $custDetailsId $PurchaseOrders`

  # print the details of the customer
  echo "Customer $mastCustId:"
  echo "Customer Details: $custDetails"
  echo "Purchase Orders: $custPO"
  echo "----------------------"
  echo
done

