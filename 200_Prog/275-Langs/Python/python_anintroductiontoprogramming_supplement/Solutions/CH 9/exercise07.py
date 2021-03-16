import Glib
# Exercise 9.05

def draw ():
    # To avoid calling SQRT test against D squared.
    d = (Glib.mouseX-100)**2 + (Glib.mouseY-100)**2
    Glib.fill(255)
    Glib.rect (100, 100, 40, 12)
    x = Glib.mouseX
    y = Glib.mouseY
    Glib.fill(0)
    if x>100 and x<140 and y>100 and y<=112:
        Glib.text ("Yes", 109, 113)
    else:
        Glib.text ("No", 112, 113)


def mouseReleased (b):
    x = Glib.mouseX
    y = Glib.mouseY
    if x>100 and x<140 and y>100 and y<=112:
        Glib.playSound(click)

width = 300
height = 300
Glib.startdraw(width, height)
Glib.background (150, 150, 255)
click = Glib.loadSound ("click.wav")
Glib.enddraw()
