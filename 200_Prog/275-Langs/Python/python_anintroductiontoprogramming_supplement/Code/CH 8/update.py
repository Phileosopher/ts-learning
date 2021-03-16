# File update to 'tmp'
from struct import *
import os

f = open("hiscores", "rb")
outf = open ("tmp", "wb")

newname = b'Karl Holter'
newscore = 100000
while True:
    try:
        s = f.read(44)
        name,score,year,month,day = unpack("32si4s2s2s", s)
        if score < newscore:
            ss = pack ("32si4s2s2s", newname, newscore, year, month, day)
            outf.write(ss)
            newscore = -1
        outf.write (s)
    except:
        break
f.close()
outf.close()
os.rename ("tmp", "hiscores")
