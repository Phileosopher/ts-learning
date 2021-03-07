import random
_xseed = 76951

def irand01 ():
    global _xseed
    _xseed = (69069*_xseed+362437) & 0xFFFFFFFF
    return _xseed

def rand01():
    return irand01()/0xFFFFFFFF


h1 = [0,0,0,0,0,0]
h2 = [0,0,0,0,0,0, 0]
for i in range (0, 10000):
    i = int(rand01()*6)
    h1[i] = h1[i] + 1
    j = random.randint(1,6)
    h2[j] = h2[j] + 1
print ("0", h1)
print (h2)

d1 = d2 = 0.0
for i in range(0, 6):
    h1[i] = h1[i]/10000.0
    d1 = d1 + (h1[i] - 10000.0/6)*(h1[i] - 10000.0/6)
    h2[i+1] = h2[i+1]/10000.0
    d2 = d2 + (h2[i] - 10000.0/6)*(h2[i] - 10000.0/6)
print (d1/10000, d2/10000)

