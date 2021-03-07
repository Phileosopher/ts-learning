# Merge sort - file

def split (n):
    f = open ("datafile.txt", "r")
    f0 = open ("tmp0.txt", "w")
    f1 = open ("tmp1.txt", "w")
    done = 0
    while done < 2:
        print ("To tmp0.txt: ", end="")
        for i in range (0, n):
            s = f.readline ()
            if s == "":
                done = done + 1
                break
            f0.write (s)
            print (s, end="")
        print()
        print ("To tmp1.txt: ", end="")
        for i in range (0, n):
            s = f.readline()
            if s == "":
                done = done+1
                break
            f1.write (s)
            print ("                 ", s, end="")
        print ()
    print (" Split complete ------------------------------")
    f1.close()
    f0.close()
    f.close()

def merge (n):
    f = open ("datafile.txt", "w")
    f0 = open ("tmp0.txt", "r")
    f1 = open ("tmp1.txt", "r")
    done = 0
    n0 = 0
    n1 = 0
    s0 = f0.readline()
    s1 = f1.readline()
    print ("Merging:")
    while done < 2:
        if s0<= s1:
            f.write(s0)
            print(s0)
            n0 = n0 + 1
            s0 = f0.readline()
            if s0 == "":
                done = done + 1
        if s1<=s0:
            f.write (s1)
            print ("                     ", s1)
            n1 = n1 + 1
            s1 = f1.readline()
            if s1 == "":
                done = done + 1

    if s0 == "":
        while s1 != "":
            f.write(s1)
            s1 = f1.readline()
    elif s1 == "":
        while s0 != "":
            f.write(s0)
            s0 = f0.readline()
    f.close()
    f1.close()
    f0.close()


n = 1
done = False
while not done:
    split (n)
    merge (n)
    n = n + 1
#    s = input()
    if n > 15: break


