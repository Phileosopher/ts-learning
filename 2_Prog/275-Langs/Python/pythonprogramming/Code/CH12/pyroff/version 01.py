# First sketch of PYROFF
from random import *

def getword (f):
    print ("Getword ")

def iscommand(w):
    print ("ISCOMMAND given ", w)
    if random()< 0.5:
        return False
    return True

def process_command (w):
    print ("Processing command ", w)

def process_word (w):
    print ("Processing the word ", w)

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
inf.close()
outf.close()
