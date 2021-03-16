# PNG
from struct import *
b2 = (137, 80, 78, 71, 13, 10, 26, 10)
types = ("Grey", "", "RGB", "Color map", "Grey with alpha", "", "RGBA")

f = open ("test.png", "rb")
s = f.read (8)               # Read the header
b1 = unpack('8B', s)
if b1 == b2:
    print ("Header OK")
else:
    print ("Bad header")

s = f.read(8)
length, type = unpack (">I4s", s)
print ("First chunk: Length is", length, "Type:", type)

s = f.read (length)
wd,ht,dep,ctype,compress, filter, interlace = unpack(">ii5B", s)
#I   I   B   B       B        B      B
print ("PNG Image width=", wd, "Height=", ht)
print ("Image has ", dep, "bytes per sample.")
print ("Color type is ", types[ctype])
if compress == 0:
    print ("Compression OK")
else:
    print ("Compression should be 0 but is", compress)
if filter==0:
    print ("Filter is OK")
else:
    print ("Filter should be 0 but is", filter)
if interlace==0:
    print ("No interlace")
elif interlace == 1:
    print ("Adam7 interlace")
else:
    print ("Bad inrlace specified: ", interlace)
f.close()