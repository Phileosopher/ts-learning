#Exercise 13.1
import smtplib
from email.mime.text import MIMEText

LOGIN = "your login"
PASSWD = "your password"


rcvr = input ("Send to what Email address:")
mtest = input("Message: ")

msg = MIMEText (mtest)
sndr = "sender"

msg['Subject'] = 'Mail from Python'
msg['From'] = sndr
msg['To'] = rcvr
print (msg)

# Send the message using Google's SMTP server.
s = smtplib.SMTP('smtp.gmail.com')  # localhost could work
print(s.starttls())
print(s.login (LOGIN, PASSWD))
print(s.send_message(msg))
print (s.quit())

