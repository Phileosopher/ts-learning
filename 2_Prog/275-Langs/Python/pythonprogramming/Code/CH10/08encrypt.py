pt = "meetyouatninepmatlocationalpha"
key = "itwasthebestoftimesitwastheworstoftimes"
ct = ""
xt = ""

print ("Plaintext is ", pt)
print ("Ciphertext is ", end="")
for i in range(0,len(pt)):
    v = ord(pt[i])^ord(key[i])
    print(v," ", end="")
    ct = ct + chr(v)
print ()

print ("Decrypted again is:", end="")
for i in range(0,len(ct)):
    v = ord(ct[i])^ord(key[i])
    print(v, " ",  end="")
    xt = xt + chr(v)
print ()
print (xt)



for i in range (0, 24):
    print (ord(ct[i]),' ',  end="")
print()
for i in range (0, 24):
    print (ord(key[i]),' ',  end="")
print()
for i in range (0, 24):
    print (ord(xt[i]),' ',  end="")
print()