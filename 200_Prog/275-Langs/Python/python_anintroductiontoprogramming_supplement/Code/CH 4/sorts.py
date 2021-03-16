import time
import random
def selectionSort (data):
  for k in range (0, len(data)):
    i = k
    for j in range (k, len(data)): #Find the min value in the remaining data
        if data[i] > data[j]:       #A new smallest value
          i = j                     #i is the smallest so far
    (data[i], data[k]) = (data[k], data[i])  # Swap values

def insertionSort (data):
    for k in range(0,len(data)):
        i = k
        while i>0 and data[i-1]>data[i]:
            (data[i],data[i-1]) = (data[i-1],data[i])
            i = i - 1


def quickSort (data, a, b):
    if (a<b):
        q = partition (data, a, b)
        quickSort (data, a, q-1)
        quickSort (data, q+1, b)

def sorted (m):
    for i in range(1,len(m)):
        if m[i-1]>m[i]:
            return False
        return True

def shuffle():
    j = len(data)
    for i in range(0, len(data)//2):
        (data[i], data[j]) = (data[j], data[i])
        j = j - 1

def partition (data, a,b):
    if a<0 or b>=len(data):
        return
    p = a          # Pivot index
    x = data[p]     # Pivot value
    i = a           # Left index
    j = b           # right index
    while i<j:      # Repeat so long as left<right
        while data[i] <= x:
            if i<b:
                i = i + 1
        while data[j] > x:
            if j>a:
                j = j - 1
        if i<j:
            (data[i], data[j]) = (data[j], data[i])
    data[a] = data[j]
    data[j] = x
    return j

def partitiona (data, a,b):
    p = (a+b)//2    # Pivot index
    x = data[p]     # Pivot value
    i = a           # Left index
    j = b-1         # right index
    while True:
        while data[j] > x:
            j = j - 1
        while data[i] < x:
            i = i + 1
        if i<j:
            (data[i], data[j]) = (data[j], data[i])
            i=i+1
        else:
    #        print (data[a:b])
            print ("Left:", data[a:j-1], "Right:", data[j:b], "Pivot ", j,data[j])
            return j

def quick(data):
    shuffle(data)
    quickSort (data, 0, len(data)-1)

s = True
Niter = 10000
while s:
    data = []
    for i in range(0,20):  # iter*20):
        data = data + [random.randint(0,100)]

    data = [17, 12, 4, 9, 7, 86, 77, 55, 13, 10, 16, 8, 100, 10, 9, 86, 21, 60, 70, 74]
    z = list(data)

    quickSort(data,0,len(data))
    if not sorted (data):
        print ("NOT SORTED", data)
        s = False

print (data)
print (z)


