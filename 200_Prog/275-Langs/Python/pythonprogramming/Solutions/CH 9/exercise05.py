import Glib
# Exercise 9.05

def draw ():
    # To avoid calling SQRT test against D squared.
    d = (Glib.mouseX-100)**2 + (Glib.mouseY-100)**2
    Glib.fill(255)
    Glib.rect (100, 100, 40, 12)
    Glib.fill(0)
    if d > 900:
        Glib.text ("No", 112, 113)
    else:
        Glib.text ("Yes", 109, 113)

def mouseReleased (b):
    print ("Nothing")

width = 300
height = 300
Glib.startdraw(width, height)
Glib.background (150, 150, 255)
Glib.enddraw()
