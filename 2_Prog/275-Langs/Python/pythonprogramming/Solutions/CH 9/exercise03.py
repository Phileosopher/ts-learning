# Exercise 9.03
import Glib
from random import *

def digit (c):
    if c>='0' and c<= '9': return True
    return False

def read_an_int (infile):
    c = infile.read(1)
    if c == "": return None
    while c == " " or c == "\n":
        c = infile.read(1)
        if c == "": return None
    v = 0
    while digit(c):
        v = v*10 + ord(c)-ord('0')
        c = infile.read(1)
    return v

def read_a_line (infile):
    x0 = read_an_int (infile)
    y0 = read_an_int (infile)
    x1 = read_an_int (infile)
    y1 = read_an_int (infile)
    if y1 == None: return None
    return (x0, y0, x1, y1)

width = 500
height = 400
lines = ()
f = open("infile.txt", "r")
c = read_a_line (f)
while c != None:
    lines = lines + (c, )
    c = read_a_line(f)
f.close()

Glib.startdraw(width, height)
Glib.background (100, 200, 100)
for L in lines:
    Glib.line (L[0], L[1], L[2], L[3])
Glib.enddraw()
