# GIF
from struct import *

f = open ("test.gif", "rb")
s = f.read (13)               # Read the header
id,  ht, wd, flags, bci,par = unpack('6shhBBB', s)
#6s  h   h     B     B   B
f.close()
id = id.decode("utf-8")
print (id)
print ("Height", ht, "Width", wd)
print("Flags:", flags)
print ("Background color index: ", bci)
print ("Pixel aspect ratio:", par)

