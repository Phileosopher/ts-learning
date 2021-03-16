# update, keeping sorted
from struct import *

searchname = "Arlen Franks"
newscore = 199999
failed = False

def printall ():
    global f, size
    for i in range (0, 13):
        f.seek(i*size)
        s=f.read(size)
        a,b,c,d,e = unpack ("32si4s2s2s", s)
        print (i, a, b)

size = 44                          # Record size
rec = 0                            # Record number


f = open ("hiscore", "r+b")       # Open the file


printall()

while True:                        # Find Arlen
    f.seek (rec*size)                #  next record)
    s = f.read(size)               #  read it
    if len(s) < size:              # End of file?
        failed = True              # Did not find teh name
        break
    a,b,c,d,e = unpack ("32si4s2s2s", s)
    name = a.decode ("UTF-8")      # Create a string
    name = name.strip('\0')        # Shorten it
    if name.strip() == searchname: # The one we want?
        break                      # Yes, exit
    rec = rec + 1                  # No, look at next
if failed:
    print ("New name, not in file.")
else:
    print ("Found", name, " at record number ", rec)
    s = pack ("32si4s2s2s",a,newscore,c,d,e)
    if rec == 0:
        if b<=newscore:
            f.seek(0)
            f.write(s)
            f.close()
            exit()

    steprec = rec
    while b<=newscore:      # New score is larger - change the file
        steprec = steprec-1      # step back
        print ("Stepped back to record ", steprec)
        f.seek (steprec*size)    # Position the file there
        ss = f.read(size)     # Read
        a,b,c,d,e = unpack ("32si4s2s2s", ss)  # Unpack
        print ("Name is ", a, "score is ", b)
        if b <= newscore:    # Still smaller?
            f.seek((steprec+1)*size)
            f.write (ss)      # Copy record further back
            if steprec == 0:
                f.seek(0)
                f.write (s)
                break
        else:
            f.seek(steprec*size) # Write new record.
            f.write (s)
            break
f.close()
