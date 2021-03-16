# Seventh sketch of PYROFF
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
    print ("Genpage")

def genline():
    print ("Genline")

def indent (n):
    global nindent
    nindent = n
    print ("Indent ", n)

def temp_indent (n):
    print ("TI ", n)

def dotl ():
    print ("DOTL")

def space (n):
    print ("Space ", n)

def process_command (w):
    global table, inf, page_length, fill, center, center_count, adjust
    global spacing, line_length, buffer
    k = table.index(w)
    if k == 0:
        s = getword(inf)
        page_length = int(s)
        print ("Page length set to ", s)
    elif k == 1:
        genpage()
    elif k == 2:
        genline()
    elif k == 3:
        fill = True
    elif k == 4:
        fill == False
    elif k == 5:
        adjust = False
    elif k == 6:
        center = True
        s = getword(inf)
        center_count = int(s)
        emit(buffer)
        buffer = ()
        print ("Center ", center_count, "lines")
    elif k == 7:
        s = getword(inf)
        spacing = int(s)
        print ("Spacing ", spacing, "lines")
    elif k == 8:
        s = getword(inf)
        line_length = int(s)
        print ("Line length ", line_length, "characters")
    elif k == 9:
        s = getword(inf)
        indent (int(s))
    elif k == 10:
        s = getword(inf)
        temp_indent (int(s))
    elif k == 11:
        hyphenate = False
    elif k == 12:
        hyphenate = True
    elif k == 13:
        dotl ()
    elif k == 14:
        s = getword(inf)
        space (int(k))

def emit (s):
    global outf
    outf.write(s+"\n")

def do_center (s):
    global line_length
    print ("Centering ", s)
    k = len(s)            # How long is the string?
    b1 = line_length - k  # How much shorter than the line?
    b2 = b1//2             # Split that amount in two
    b1 = line_length - k - b2
    s = " "*b1 + s + " "*b2  # Add spaces to center the text
    print (b1, b2, s)
    emit(s)                  # Write to file

def process_word (w):
    global buffer, line_length, clast, center, center_count

    if center:                 # Text is being centered, no fill
        if len(buffer) > 0:            # Add this word to the line
            buffer = buffer + " " + w
        else:
            buffer = w
        if clast == "\n":
            do_center(buffer)                # Emit the text
            buffer = ""                      # Clear the buffer
            center_count = center_count - 1  # Count lines
            if center_count <= 0:            # Done?
                center = False               # Yes. Stop centering.

    else:
        if len(buffer) + len(w) + 1 <= line_length:
            if len(buffer) > 0:
                buffer = buffer + " " + w
            else:
                buffer = w
        else:
            emit(buffer)
            buffer = w


page_length	= 55	    # Number of lines of text on a single page
fill		= True	    # Controls whether the text is being formatted
adjust		= True	    # Controls whether the text if right justified
center		= False	    # Controls whether text is being centered
center_count	= 0	    # Number of lines still to be centered
spacing		= 1	        # Number of lines output per line of text
nindent		= 0	        # Number of spaces on the left
line_length	= 66	    # Number of characters on one line
hyphenate	= True	    # Are words hyphenated by the system?
buffer = ""

c = " "
clast = c2last = c
filename = "source.txt" #input ("PYROFF: Enter the name if the input file: ")
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
