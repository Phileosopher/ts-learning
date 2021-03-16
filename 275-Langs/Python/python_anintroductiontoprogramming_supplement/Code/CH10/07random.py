import time
_xseed = 76951

def irand01 ():
    global _xseed
    _xseed = (69069*_xseed+362437) & 0xFFFFFFFF
    return _xseed

def rand01():
    return irand01()/0xFFFFFFFF

def setseed (x):
      global _xseed
      _xseed = x

def randrange (n1, n2):
    x = (int) (rand01()*(n2-n1+1)) + n1
    return x

def randomize ():
    global _xseed
    _xseed = int(time.time ()) & 0xFF

rolls = [0,0,0,0,0,0,0]
randomize()
for i in range (0,10):
#    i = int(rand01()*6 + 1)
    i = randrange (2, 4)
    print (i)
print (time.gmtime(0) )
