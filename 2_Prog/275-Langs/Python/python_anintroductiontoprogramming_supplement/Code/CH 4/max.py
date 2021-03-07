# Module max.py

def maxr (myList):
    m1 = myList[0]
    if len(myList)>1:
        m2 = maxr (myList[1:])
    else:
        return m1
    if m1 > m2:
        return m1
    else:
        return m2

def max (myList):
    max = myList [0]
    for i in range(1, len(myList)):
        if myList[i] > max:
            max = myList[i]
    return max


