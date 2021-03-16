#from random import *
#import struct

from array import array
out = open('ints', 'wb')
arr = array('i')
for k in range (10000, 20000):
    arr.append(k)
arr.tofile(out)
print ("Arr is ", len(arr))
out.close()

# Read them back
inf = open ('ints', 'rb')
arrin = array('i')
for k in range (0, 10001):
    try:
        arrin.fromfile(inf, 1)
    except:
        break
    print (arrin[k])
inf.close()

