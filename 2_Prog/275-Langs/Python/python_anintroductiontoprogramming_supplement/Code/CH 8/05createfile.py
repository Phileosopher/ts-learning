# Create hiscore file
from struct import *

f = open ("hiscores", "wb")
name = bytes("Jim Parker", 'UTF-8')
score = 109800
year = b"2015"
month = b"12"
day = b"26"

s = pack ("32si4s2s2s", name, score, year, month, day)
print (type(s), s)
f.write(s)

name = bytes("Ben Issac", 'UTF-8')
score = 107800
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)

name = bytes("Valentine Ivo", 'UTF-8')
score = 107000
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
name = bytes("Graeme Roswell", 'UTF-8')
score = 105500
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
name = bytes("Ben Issac", 'UTF-8')
score = 105300
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
name = bytes("Ken Sterling", 'UTF-8')
score = 107800
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
name = bytes("Gottlob Wilmer", 'UTF-8')
score = 102100
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
name = bytes("Dennis Brand", 'UTF-8')
score = 100900
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
name = bytes("Arlen Franks", 'UTF-8')
score = 100100
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
name = bytes("Calvin Merlyn", 'UTF-8')
score = 99000
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
name = bytes("Gregg Skyler", 'UTF-8')
score = 92100
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
name = bytes("Reggie Lynton", 'UTF-8')
score = 87800
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
name = bytes("Avery Smith", 'UTF-8')
score = 87600
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
name = bytes("Jane Diamond", 'UTF-8')
score = 86300
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
name = bytes("Neville Jameson", 'UTF-8')
score = 85900
s = pack ("32si4s2s2s", name, score, year, month, day)
f.write(s)
f.close()
