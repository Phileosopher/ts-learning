from random import *
class value:
    def __init__ (self):
        self.val = randrange(0,100)

t = ()
for i in range(0,100):
    v = value()
    t = t + (v,)
s = 10000
for i in range(0, 100):
#    print (t[i].val)
    if t[i].val < s:
        s = t[i].val
print ("Minimum is ", s)