# Selection sort

data = [12, 18, 5, 21, 9]

def selection (data):
    for istart in range (0, len(data)-1):
        imin = istart
        for i in range(istart,len(data)):
            if data[i] < data[imin]:
                imin = i
        (data[istart], data[imin]) = (data[imin], data[istart])
selection (data)
print(data)