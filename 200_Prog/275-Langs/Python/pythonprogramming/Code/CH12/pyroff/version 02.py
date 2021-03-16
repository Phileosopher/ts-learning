# First sketch of PYROFF
from random import *

def whitespace (c):
    if c == " ": return True
    if c == "\t": return True
    if c == "\n": return True
    return False

def ch(f):
    global c
    return (c)

def nextch(f):
    global c
    c = f.read(1)

def getword(f):
    w = ""
    while whitespace(ch(f)):
        nextch(f)
    while not whitespace(ch(f)) and ch(f) !="":
        w = w + ch(f)
        nextch(f)
    return w

def iscommand(w):
#    if random()< 0.5:
    return False

def process_command (w):
    print ("Processing command ", w)

def process_word (w):
    print (w)

c = " "
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
