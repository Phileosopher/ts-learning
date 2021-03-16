# read and print hiscore file
from struct import *

f = open ("hiscores", "rb")
while True:
    try:
        s = f.read(44)
        name,score,year,month,day = unpack("32si4s2s2s", s)
        name = name.decode("UTF-8")
        year = year.decode("UTF-8")
        month = month.decode("UTF-8")
        day = day.decode("UTF-8")
        print (name, score, year, month, day)
    except:
        print ("-------------- Done -----------------")
        break
f.close()
