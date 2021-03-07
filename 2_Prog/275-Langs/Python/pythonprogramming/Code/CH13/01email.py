# Import smtplib for the actual sending function
import smtplib

LOGIN = "your email"
PASSWD = "your password"

me = "sender"
you = "receiver"

msgt = "From: user_me@gmail.com\n"
msgt = msgt + "To: user_you@gmail.com\n"
msgt = msgt + "Subject: Just a message\n"
msgt = msgt + "\n"
msgt = msgt + "Attention: This message was sent by Python!\n"
try:
    server = smtplib.SMTP('smtp.gmail.co')
except:
    print ("Error occured. Can't connect")
else:
    server.starttls()
    server.login(LOGIN,PASSWD)
    server.sendmail(me, you, msgt)
    print (msgt)
    server.quit()