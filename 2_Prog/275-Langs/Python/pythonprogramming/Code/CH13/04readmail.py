import poplib
import getpass

mServer = poplib.POP3('server')
print (mServer)
#Login to mail server
mServer.user("your email")
mServer.pass_("your password")

#Get the number of mail messages
numMessages = len(mServer.list()[1])

print ("You have %d messages." % (numMessages))
print ("Message List:")

#List the subject line of each message
for mList in range(numMessages) :
    for msg in mServer.retr(mList+1)[1]:
#        if msg.startswith('Subject'):
        print ("** ", msg)
        if msg[0:6] == "Subject":
            print ('\t' + msg)
            break

mServer.quit()