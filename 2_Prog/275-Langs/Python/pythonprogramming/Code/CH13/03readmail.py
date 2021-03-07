# IMAP
import imaplib

server = 'imap.gmail.com'          # IMAP Server
USER = "your email"  # USER ID
PASSWORD = "your password"            # Mask this password
EMAIL_FOLDER = "Inbox"             # Which mailbox?

mbox = imaplib.IMAP4_SSL(server)   # Connect
mbox.login(USER, PASSWORD)         # Authenticate

env, data = mbox.select(EMAIL_FOLDER)  # Select the mailbox
if env == 'OK':                        # Did it work?
    print ("Printing subject headers: ", EMAIL_FOLDER)

    env, data = mbox.search(None, "ALL")  # Select the messages wanted.
    if env != 'OK':                       # Are there any?
        print ("No messages.", env)       # Nope.
        exit()

    for num in data[0].split():          # For each selected message b'1 2 3 ...'
        (env, data) = mbox.fetch(num, '(RFC822.HEADER)')  # Read it
        if env != 'OK':
            print ("ERROR getting message", num, ", ", env)
            break
        s = str(data[0][1])        # Look for the string "Subject" in the header
        k = s.find("Subject")
        if (k>=0):                 # Found it?
            s =  s[k:]             # Extract the string to the next '\r'
            k = s.find('\\r')
            s = s[:k]
            print (s)              # And print it.
    mbox.close()
else:
    print ("No such mailbox as ", EMAIL_FOLDER)
mbox.logout()
