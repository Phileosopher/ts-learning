
name = ["Adams", "Carlson", "Dennison", "Fink", "Howe", "Kelly", "Niven", "Oneil"]
number=[20,      19,        45,          36,    29,     55,      8,       61]
rank=  [12,      32,        14,          76,    66,     108,     47,      85]
t200 = [107,    112,       108,         110,    113,    116,     114,     121]


for istart in range (0, len(name)-1):
    imin = istart
    for i in range(istart,len(name)):
        if t200[i] < t200[imin]:
            imin = i
    (name[istart], name[imin]) = (name[imin], name[istart])
    (t200[istart], t200[imin]) = (t200[imin], t200[istart])
    (number[istart], number[imin]) = (number[imin], number[istart])
    (rank[istart], rank[imin]) = (rank[imin], rank[istart])

for i in range (0, len(name)):
    print (i+1,  name[i], number[i], t200[i], rank[i])
