# Ninth sketch of PYROFF
from random import *

table = (".pl", ".bp", ".br",".fi",".nf",".na",".ce",
         ".ls", ".ll", ".in",".ti",".nh",".hy",".tl", ".sp")

def whitespace (c):
    global lastws
    if c == " ": return True
    if c == "\t": return True
    if c == "\n": return True
    return False

def ch(f):
    global c
    return (c)

def nextch(f):
    global c, clast, c2last
    c = f.read(1)
    if whitespace(c):
        c2last = clast
        clast = c

def getword(f):
    w = ""
    while whitespace(ch(f)):
        nextch(f)
    while not whitespace(ch(f)) and ch(f) !="":
        w = w + ch(f)
        nextch(f)
    return w

def iscommand(w):
    global table, c2last
    if c2last == "\n":
        if w in table:
            return True
    return False

def genpage():
    global page_length, lines
    lbreak()
    for i in range (lines, page_length):
        emit ("")

def lbreak ():
    global buffer, tempindent, nindent
    if len(buffer) > 0:
        emit(buffer)
#    buffer = " "*(nindent+tempindent)
    buffer = ""

def indent (n):
    global nindent, buffer
    nindent = n
    emit(buffer)
    buffer = ""

def temp_indent (n):
    global buffer, tempindent
    tempindent = n
    lbreak()

def space (n):
    global buffer
    lbreak()
    for i in range (0,n):
        emit(buffer)

def process_command (w):
    global table, inf, page_length, fill, center, center_count, adjust
    global spacing, line_length, buffer, hyphenate
    k = table.index(w)
    if k == 0:
        s = getword(inf)
        page_length = int(s)
    elif k == 1:
        genpage()
    elif k == 2:
        lbreak()
    elif k == 3:
        fill = True
    elif k == 4:
        fill = False
    elif k == 5:
        adjust = False
    elif k == 6:
        center = True
        s = getword(inf)
        center_count = int(s)
        if center_count<=0:  # Possible user error
            center_count = 0
            center = False
        emit(buffer)
        buffer = ""
    elif k == 7:
        s = getword(inf)
        spacing = int(s)
        if spacing <=0:       # Possible user error
            spacing = 1
    elif k == 8:
        s = getword(inf)
        kk = int(s)
        if kk>0 and kk<80:    # Possible user error
            line_length = int(s)
    elif k == 9:
        s = getword(inf)
        kk = int(s)
        if (kk>=0):           # Possible user error
            indent (kk)
    elif k == 10:
        s = getword(inf)
        kk = int(s)
        if kk>0:              # Possible user error
            temp_indent (kk)
    elif k == 11:
        hyphenate = False
    elif k == 12:
        hyphenate = True
    elif k == 13:
        print ("Command removed")
    elif k == 14:
        s = getword(inf)
        kk = int(s)
        if kk > 0:           # Possible user error
            space (int(kk))

def emit (s):
    global outf, lines, tempindent, spacing, page_length
    outf.write(s+"\n")
    lines = (lines + 1)%page_length
    for i in range (2, spacing):
        outf.write ("\n")
        lines = (lines + 1)%page_length
    tempindent = 0

def do_center (s):
    global line_length
    k = len(s)            # How long is the string?
    b1 = line_length - k  # How much shorter than the line?
    b2 = b1//2             # Split that amount in two
    b1 = line_length - k - b2
    s = " "*b1 + s + " "*b2  # Add spaces to center the text
    emit(s)                  # Write to file

def nth_space (s, ii, n):
    global nindent, tempindent
    nn = 0
    i = ii
    while True:
        if s[i] == " ":
            nn = nn + 1
        if nn >= n:
            return i
        i = (i + 1)%len(s)
        if i < nindent+tempindent:
            i = nindent+tempindent

def process_word (w):
    global buffer, line_length, clast, center, center_count
    global nindent, tempindent
    if center:                   # Text is being centered, no fill
        if len(buffer) > 0:            # Add this word to the line
            buffer = buffer + " " + w
        else:
            buffer = " "*(nindent+tempindent) +w
#            tempindent = 0
        if clast == "\n":
            do_center(buffer)                 # Emit the text
            buffer = " "*(nindent+tempindent) # Clear the buffer
#            tempindent = 0
            center_count = center_count - 1   # Count lines
            if center_count <= 0:             # Done?
                center = False                # Yes. Stop centering.

    elif not fill:
        if len(buffer) > 0:            # Add this word to the line
            buffer = buffer + " " + w
        else:
            buffer = " "*(nindent+tempindent) +w
            tempindent = 0
        if clast == "\n":
            emit(buffer)
            buffer = ""

    elif adjust:
        k = line_length - len(buffer)   # Number of spaces remaining
        if k  > len(w):                 # Does the word w fit?
            if len(buffer) == 0:        # Yes. Empty buffer?
                buffer = " "*(nindent+tempindent) +w  # Yes. Buffer = word.
#                tempindent = 0
            else:                       # No. Add word to the buffer
                buffer = buffer + " " + w
        else:                           # Not enough space remains
            nspaces = buffer.count(" ") # How many spaces in buffer?
            xk = k + (k+1)//2             # Space insert increment
            if k%2 == 0:                # make it odd
                xk = xk+1
            while k > 0:
                i = nth_space (buffer, 0, xk)
                while i < nindent+tempindent:
                    i = nth_space (buffer, i, xk)
                buffer = buffer[0:i] + " " + buffer[i:]
                k = k - 1
            emit(buffer)
            buffer = " "*(nindent+tempindent) +w
#            tempindent = 0
    else:
        if len(buffer) + len(w) + 1 <= line_length:
            if len(buffer) > 0:
                buffer = buffer + " " + w
            else:
                buffer = " "*(nindent+tempindent) +w
#                tempindent = 0
        else:
            emit(buffer)
            buffer = " "*(nindent+tempindent) +w
#            tempindent = 0

page_length	= 63	    # Number of lines of text on a single page
fill		= True	    # Controls whether the text is being formatted
adjust		= True	    # Controls whether the text if right justified
center		= False	    # Controls whether text is being centered
center_count	= 0	    # Number of lines still to be centered
spacing		= 1	        # Number of lines output per line of text
nindent		= 0	        # Number of spaces on the left
tempindent = 0          # Number of temporary indent spaces
line_length	= 66	    # Number of characters on one line
hyphenate	= True	    # Are words hyphenated by the system?
buffer = ""
c = " "
clast = "\n"
c2last = "\n"
lines = 0

filename = input ("PYROFF: Enter the name if the input file: ")
inf = open (filename, "r")
outf = open ("pyroff.txt", "w")
w = getword (inf)

while w != "":
    if iscommand(w):
        process_command (w)
    else:
        process_word (w)
    w = getword(inf)

if len(buffer) >0:
    emit(buffer)
inf.close()
outf.close()
