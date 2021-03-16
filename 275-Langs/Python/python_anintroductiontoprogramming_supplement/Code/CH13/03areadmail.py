# IMAP
import imaplib

server = 'imap.gmail.com'
USER = "your email"
PASSWORD = "your password"            # Mask this password
EMAIL_FOLDER = "Inbox"

def dump_subjects(m):

    env, data = m.search(None, "ALL")
    if env != 'OK':
        print ("No messages.", env)
        return
    print ("RV is ", env, " Data[0] is ", data[0])

    for num in data[0].split():
        env, data = m.fetch(num, '(UID BODY[TEXT])')
        if env != 'OK':
            print ("ERROR getting message", num, ", ", env)
            return
        s = str(data[0][1])
        slist = s.split("\\r\\n")
        for i in range(0,len(slist)):
            s = slist[i]
            k = s.find("Subject")
            if (k>=0):
                print (s[k:])
                break

mbox = imaplib.IMAP4_SSL(server)
mbox.login(USER, PASSWORD)
env, data = mbox.select(EMAIL_FOLDER)
if env == 'OK':
    print ("Printing subject headers: ", EMAIL_FOLDER)
    dump_subjects(mbox)
    mbox.close()
else:
    print ("No such mailbox as ", EMAIL_FOLDER)
mbox.logout()
