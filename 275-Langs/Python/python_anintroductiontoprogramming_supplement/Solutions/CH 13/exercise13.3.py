from ftplib import FTP

def myprint (ss):
    global outfile, outstring
    s = str(ss)
    f = open (outfile, "w")
    outstring = outstring + s
    print (len(s),s)
    f.close()

def dump (fname, data):
    f = open (fname, "w")
    f.write(data)
    f.close()

try:
    ftp = FTP("Your ftp site here")
except:
    print ("No such site")
print (ftp.login())
print(ftp.retrlines("LIST"))

outfile = "one.txt"
outstring = ""
ftp.retrlines('RETR one.txt', myprint)
dump (outfile, outstring)

outfile = "two.txt"
outstring = ""
ftp.retrlines('RETR two.txt', myprint)
dump (outfile, outstring)

outfile = "three.txt"
outstring = ""
ftp.retrlines('RETR three.txt', myprint)
dump (outfile, outstring)

ftp.quit()
