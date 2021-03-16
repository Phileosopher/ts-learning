list1 = ["Hydrogen","Helium","Lithium","Beryllium","Boron","Carbon"]
s = input("Enter:")
try:
    list1.remove(s)
except:
   print ('Can’t find ', s)
print (list1)
