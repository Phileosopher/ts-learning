# from Glib import *
# import Glib
#
# def draw ():
#     background(200)
#     ellipse (Glib.mouseX, Glib.mouseY,  30, 30)
#
# startdraw(400, 400)
# fill (255, 0, 0)
# enddraw()



from Glib import *
import Glib

def initialize ():
    fill (255, 0, 0)

def draw ():
    background(200)
    ellipse (Glib.mouseX, Glib.mouseY,  30, 30)

startdraw(400, 400)
enddraw()
