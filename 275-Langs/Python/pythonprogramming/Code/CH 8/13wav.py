# WAV
from struct import *

f = open("test.wav", "rb")
s = f.read (12)
riff,sz,fmt = unpack ("4si4s", s)
riff = riff.decode("utf-8")
fmt = fmt.decode("utf-8")
print (riff, sz, "bytes ", fmt)

s = f.read (24)
id, sz1, fmt,nchan,rate,bytes,algn, bps = unpack ("4sihhiihh", s)
#4s  i    h    h    i    i     h    h
id = id.decode ("utf-8)")
print ("ID is", id, "Channels ", nchan, "Sample rate is ", rate)
print ("Bits per sample is ", bps)
if fmt==1:
    print ("File is PCM")
else:
    print ("File is compressed ", fmt)
print ("Byterate was ", bytes, "should be ", rate*nchan*bps/8)

