def fprint (s, *vlist):
    i = 0
    if len(s) != len(vlist):
        print ("There must be the same number of variables as format items.")
        return
    for v in vlist:
        if s[i] == "f":
            fv = float(v)
            print (fv, " ", end="")
        elif s[i] == "i":
            iv = int(v)
            print(iv, " ", end="")
        else:
            print ("?", end="")
        i = i + 1


fprint ("iiff", 12, 13, 14, 15)