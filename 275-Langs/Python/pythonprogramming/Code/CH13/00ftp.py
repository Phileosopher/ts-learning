from ftplib import FTP

def myprint (ss):
    s = str(ss)
    x = s.split("\\n")
    for i in range (0, len(x)):
        print (x[i])

try:
    ftp = FTP("ftp site here")
except:
    print ("No such site")
    ftp.login()
    ftp.retrlines("LIST")
    ftp.retrlines('RETR README', myprint)
    ftp.quit()

