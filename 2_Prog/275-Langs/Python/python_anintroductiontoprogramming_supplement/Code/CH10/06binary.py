import time

def search (list, target):
    istart = 0
    k = 0
    iend = len(list)
    while istart<=iend:
        m = (iend+istart)//2
#        print ("Start ", istart, " end ", iend, " m ", m, " v ", list[m])
        if list[m]>target:
            iend = m-1
        elif list[m]<target:
            istart = m+1
        else:
            return m
    return None

x = [10982, 12534, 12856, 18756, 19872, 29765, 56344, 87656, 88768, 90012]
t0 = time.clock()
for count in range (0, 100000):
    k = 90012 in  x
    k = x.index(90012)
t1 = time.clock()
print ("Builtin index ", (t1-t0)/100000)


target = 90012
t0 = time.clock()
n = len(x)
for count in range (0, 100000):
        istart = 0
        k = 0
        iend = n
        while istart<=iend:
            m = (iend+istart)//2
            if x[m]>target:
                iend = m-1
            elif x[m]<target:
                istart = m+1
            else:
                break
t1 = time.clock()
print ("Function was ", (t1-t0)/100000)