# RSA Key determination
import math
from fractions import gcd

def eea(a, b) :
    if b == 0 :
        return (1,0,a)
    else :
        (aa, bb, g) = eea(b, a % b)
        return (bb, aa - bb * (a // b),g)

def modular_inverse(a,m) :
    x,y,gcd = eea(a,m)
    if gcd == 1 :
        return x % m
    else :
        return None

def search_modular_inverse (e, j):
    d = 0
    for i in range (3, j):
        if (i*e)%j == 1:
            d = i
            break
    return d

p = 73
q = 83
#p = 61
#q = 53

n = p*q
j = (p-1)*(q-1)

print ("n is ", n, " and psi is ", j)

for i in range (14, n):  # Test this better
    if gcd(i, n) == 1:
        e = i
        break
    print (i, " ... no")
e = 17
print ("e is ", e)


d = search_modular_inverse (e, j)
print ("Searched ", e, d, e*d % j)

d = modular_inverse (e, j)
print ("Computed ", e, d, e*d % j)


print ("The public key is (", e, ",", n, ")")
print ("The private key is (", d, ")")

message = "Depart at dawn"
imessage = ()
cmessage = ()
for i in range (0, len(message)):
    m = ord(message[i])
    imessage = imessage +(ord(message[i]),)
    c = (m**e) % n
    cmessage = cmessage + (c,)
print ("The message is ", imessage)
print ("The encrypted message is ", cmessage)

dmessage = ()
for i in range (0, len(cmessage)):
    c = cmessage[i]
    m = (c ** d) % n
    dmessage = dmessage + (m, )

#dmessage = (cmessage**d) % n
print ("Decrypted message is ", dmessage)

