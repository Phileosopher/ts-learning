# read and print hiscore file
from struct import *

f = open ("hiscores", "r+b")
pos = 44*8
f.seek(pos)
s = f.read(44)
name = b'Arlen Franks'
score = 100300
year = b'2015'
month = b'12'
day = b'26'
ss = pack("32si4s2s2s", name,score, year,month,day)
print (score, "...........")
f.seek (44*8)
f.write(ss)
f.close ()
