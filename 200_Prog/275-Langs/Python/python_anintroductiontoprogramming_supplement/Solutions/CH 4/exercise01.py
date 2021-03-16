# Exercise 4.1

def maxi (t):
    imax = 0
    for i in range(1,len(t)):
        if t[i] > t[imax]:
            imax = i
    return (imax)

print (maxi( (2,4,121,9,99,12,18) ))