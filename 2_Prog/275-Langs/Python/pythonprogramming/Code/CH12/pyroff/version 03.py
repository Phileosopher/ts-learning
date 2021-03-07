# Third sketch of PYROFF
from random import *

table = (".pl", ".bp", ".br",".fi",".nf",".na",".ce",
         ".ls",".ll",".in",".ti",".nh",".hy",".tl",)

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

def process_command (w):
    print ("Processing command ", w)

def process_word (w):
    print (w)

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

inf.close()
outf.close()
