# Merge sort

data = [12, 18, 5, 21, 9]

def mergesort (data):
    n = len(data)
    if n <= 1:
        return
    middle = n//2
    lower = data[:middle]
    upper = data[middle:]
    mergesort(upper)
    mergesort(lower)

    (i,j,k) = (0,0,0)
    while i < len(lower) and j < len(upper):
        if lower[i] < upper[j]:
            data[k]=lower[i]
            i=i+1
        else:
            data[k]=upper[j]
            j=j+1
        k=k+1

    for i in range (i,len(lower)):
        data[k] = lower[i]
        k = k + 1
    for j in range (j, len(upper)):
        data[k] = upper[j]
        k = k + 1


alist = [54,26,93,17,77,31,44,55,20]
mergesort(alist)
print(alist)
