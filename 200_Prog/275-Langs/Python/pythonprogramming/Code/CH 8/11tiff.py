# TIFF
from struct import *

f = open ("test.tif", "rb")
s = f.read (8)                    # Read the IFH
id,  ver, off = unpack('2shL', s)
#2s   h    L

id = id.decode("utf-8")
print ("TIFF ID is ", id, end="")
if id == "II":
    print ("which means little-endian.")
elif id == "mm":
    print ("which means big-endian")
else:
    print ("which means this is not a TIFF.")
print ("Version", ver)
print("Offset", off)

f.seek(off)                     # Get the first IFD
n = 0
b = f.read (2)                  # Number of tags
n = b[0] + b[1]*256
#n = int(s.decode("utf-8"))
for i in range(0,n):
    s = f.read (12)             # Read a tag
    id,dt,dc,do = unpack ("hhLL", s)
    print ("Tag ", id, "type", dt, "count", dc, "Offset", do)
f.close()