from Glib import *

s = ""
t = ""

def keyPressed(k):
    global s, t
    if k == K_RETURN:
        t = s
        s = ""
        return
    if k == K_BACKSPACE and len(s)>0:
        s = s[0:len(s)-1]
    else:
        s = s + chr(k)


def draw ():
    global s, t
    background (200)
    text ("Enter a string: ", 10, 100)
    text (s, 20, 130)
    if (t != ""):
        text ("Completed string is "+t, 20, 150)

startdraw(200, 200)
enddraw()
