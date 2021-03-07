# Longest common subsequence

def matout (m):
    global s1, s2
    nc = len(s1)+1
    nr = len(s2)+1
    print ("  "+s1)
    print (" ", end="")

    for j in range (0,nr):
        for i in range(0, nc):
            print (m[i][j], end="")
        print ()
        if j<len(s2): print (s2[j], end="")

def max (a,b,c,d):
    if a>=b and a>=c and a>=d:
        return a
    if b>=a and b>=c and b>=d:
        return b
    if c>=a and c>=b and c>=d:
        return c
    return d

def smith (s1, s2):
    global T, gap_penalty
    for j in range (1, len(s2)+1):
        for i in range (1, len(s1)+1):
            if s1[i-1]==s2[j-1]:
                sigma = 2
            else:
                sigma = -2
            t1 = T[i-1][j-1]+sigma
            t2 = T[i-1][j]+gap_penalty
            t3 = T[i][j-1]+gap_penalty
            t4 = 0
            T[i][j] = max (t1, t2, t3, t4)
        matout(T)
    return None

def backtrack():
    global s1, s2
    mi = 0
    mj = 0
    maxv = T[mi][mj]
    for j in range (1, len(s2)+1):
        for i in range (1, len(s1)+1):
            if T[i][j] >= maxv:
                maxv = T[i][j]
                mi = i
                mj = j
    print ("Max value is ", T[mi][mj], " at (", mi, ",", mj, ")")
    m1 = ""
    m2 = ""
    print ("s1 is '", s1, "' length ", len(s1))
    while mi>0 or mj>0:
        t11 = T[mi-1][mj-1]  # Diagonal
        t01 = T[mi][mj-1]    # Up
        t10 = T[mi-1][mj]    # Left
        print (":: ", t11, "   ", t01)
        print (":: ", t10, "   ", T[mi][mj])
        if t11>=t01 and t11 >= t10:      # Diagonal is best
            m1 = s1[mi-1] + m1
            m2 = s2[mj-1] + m2
            mi = mi - 1
            mj = mj - 1
            print ("Diagonal", m1, m2)
        elif t01>t11 and t01 > t10:    # UP is best
            m1 = s1[mi-1] + m1
            m2 = "_" + m2
            mj = mj - 1
            print ("  UP  ")
        elif t10>t11 and t10>t01:     # Left is best
            m1 = "_"+m1
            m2 = s2[mj-1]+m2
            mi = mi - 1
            print (" LEFT ")
        else:
            m1 = s1[mi-1] + m1
            m2 = s2[mj-1] + m2
            mi = mi - 1
            mj - mj - 1
            print (" MISMATCH ")
    if mi>0:
        m1 = s1[0:mi]+m1
    if mj > 0:
        m2 =  s2[0:mj] + m2
    print ("M1 ", m1)
    print ("M2 ", m2)




s1 = "CTCGCAGC"
s2 = "CATTCAC"
s1 = "ATTATC"
s2 = "ATCAT"
s1 = "AGGACAT"
s2 = "ATTACGAT"
gap_penalty = -1


T = [0 for i in range(0,len(s1)+1)]
for i in range(0, len(s1)+1):
    T[i] = [0 for j in range(0,len(s2)+1)]
matout (T)

# Test
smith(s1, s2)
matout(T)
backtrack()

