#********************************************************************
# The Tkinter version of the graphics library - no sound or video
# Need tkinter module, standard user interface library
from tkinter import *

# To-Do:  1. Symbolic names for special charaters (LEFT, RIGHT, etc)

# http://zetcode.com/gui/tkinter/drawing/
# These are global variables that are used by the user or are phantoms
width = 100                   # Default canvas width
height = 100                  # Default canvas height
_fillcol = "#ffffff"            # Current fill color
_strokecol = "#000000"                # Current stroke color
_bgcol = "#a0a0a0"              # Current background color
_ELLIPSEMODE = 0              # Mode for drawing an ellipse
CENTER = 0                    # 0 = center
RADIUS = 1                    # 1 = radius
CORNER = 2                    # 2 = corner
CORNERS = 3                   # 3 = corners
_RECTMODE = CORNER            # Mode for drawing rectangles
mouseX = 0                    # X position of the mouse right now
mouseY = 0                    # Y position of the mouse right now
_dofill = True                # Should polygons be filled?
_dostroke = True              # Should polygons be outlined?
_linewidth = 1                # Line width in pixels
Arc = ARC
Pieslice = PIESLICE
Chord = CHORD
_hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
_font_family = "Times"
_font_size = 12
_font_weight = "normal"
_font_slant = "roman"
myfont = None

BLACK = "#000000"
WHITE = "#ffffff"
RED = "#ff0000"
GREEN = "#00ff00"
BLUE = "#0000ff"
BACKSPACE = '\b'
font = None
canvas = 0

def Width():
    global width
    return width

def Height():
    global height
    return height

#  Turn on filling. Set the fill color for polygons, text color too.                **
def fill(r, g=1000, b=1000):
    global _fillcol, _dofill
    _dofill = True
    if g == 1000:
        _fillcol = cvtColor3(r, r, r)
    else:
        _fillcol = cvtColor3 (r, g, b)
   
# Turn filling off.                                                                 
def nofill():
    global _dofill
    _dofill = False

# Set the line and outline color.                                                   
def stroke(r, g=1000, b=1000):
    global _strokecol, _dostroke
    if g == 1000:
        _strokecol = cvtColor3(r, r, r)
    else:
        _strokecol = cvtColor3(r, g, b)
    _dostroke = True

# Turn off outline drawing.                                                         
def nostroke():
    global _dostroke
    _dostroke = False

# Set the mode for drawing ellipses.                    
def ellipsemode(z):
    global _ELLIPSEMODE
    _ELLIPSEMODE = z

# Draw an ellipse. Also used for circles. Four modes as described in doc
# NOTE: Objects are given the tag _P so that they can be destroyed after each frame 
def ellipse(xpos, ypos, width, height):
    global canvas, _ELLIPSEMODE

    if _ELLIPSEMODE == CENTER:  # Mode 0 is CENTER
        if _dofill:
            canvas.create_oval(xpos-width/2, ypos-height/2, xpos+width/2, ypos+height/2, fill=_fillcol)
        if _dostroke:
            if width//2 < _linewidth:
                width = _linewidth*2
            if height//2 < _linewidth:
                height = _linewidth*2
            canvas.create_oval(xpos-width/2, ypos-height/2, xpos+width/2, ypos+height/2, fill="", outline=_strokecol)
    elif _ELLIPSEMODE == RADIUS: # Mode 1 is Radius
        if _dofill:
            canvas.create_oval(xpos-width, ypos-height, xpos+width, ypos+height, fill=_fillcol)
        if _dostroke:
            canvas.create_oval(xpos-width, ypos-height, xpos+width, ypos+height, fill="", outline=_strokecol)
    elif _ELLIPSEMODE == CORNER:
        if _dofill:
            canvas.create_oval(xpos, ypos, xpos+width, ypos+height, fill=_fillcol)
        if _dostroke:
            canvas.create_oval(xpos, ypos, xpos+width, ypos+height, fill="", outline=_strokecol)
    elif _ELLIPSEMODE == CORNERS:
        if _dofill:
            canvas.create_oval(xpos, ypos, width, height, fill=_fillcol)
        if _dostroke:
            canvas.create_oval(xpos, ypos, width, height, fill="", outline=_strokecol)
    else:
        print("Error: Illegal value for ELLIPSEMODE", _ELLIPSEMODE)  # 101
  
# Draw a line                                                                      
def line(x0, y0, x1, y1):
    global canvas, _strokecol
    canvas.create_line((x0, y0, x1, y1), fill=_strokecol, width=_linewidth)

# Draw a point.                                                                    
def point(x, y):
    global _fillcol
    canvas.create_line((x, y, x+1, y), fill=_fillcol)

# Draw a rectangle. Same 4 modes as ellipse.                                       
def rect(xpos, ypos, x2, y2):
    global canvas, _RECTMODE
    if _RECTMODE == CENTER:  # Mode 0 is CENTER
        if _dofill:
            canvas.create_rectangle(xpos-x2/2, ypos-y2/2, xpos+x2/2, ypos+y2/2, fill=_fillcol)
        if _dostroke:
            canvas.create_rectangle(xpos-x2/2, ypos-y2/2, xpos+x2/2, ypos+y2/2, fill="", outline=_strokecol)
    elif _RECTMODE == RADIUS:      # RADIUS mode
        if _dofill:
            canvas.create_rectangle(xpos-x2, ypos-y2, xpos+x2, ypos+y2, fill=_fillcol)
        if _dostroke:
            canvas.create_rectangle(xpos-x2, ypos-y2, xpos+x2, ypos+y2, fill="", outline=_strokecol)
    elif _RECTMODE == CORNER:      # CORNER mode
        if _dofill:
            canvas.create_rectangle(xpos, ypos, xpos+x2, ypos+y2, fill=_fillcol)
        if _dostroke:
            canvas.create_rectangle(xpos, ypos, xpos+x2, ypos+y2, fill="", outline=_strokecol)
    elif _RECTMODE == CORNERS:  #CORNERS
        if _dofill:
            canvas.create_rectangle(xpos, ypos, x2, y2, fill=_fillcol)
        if _dostroke:
            canvas.create_rectangle(xpos, ypos, x2, y2, fill="", outline=_strokecol)
    
# Draw a triangle specified by three points.                                       
def triangle (x0,y0, x1,y1, x2,y2):
    global canvas, _fillcol
    if _dofill:
        canvas.create_polygon(((x0, y0), (x1, y1), (x2, y2)), fill=_fillcol)
    if _dostroke:
        canvas.create_polygon(((x0, y0), (x1, y1), (x2, y2)), fill="", outline=_strokecol)


def bold():
    global font_weight
    _font_weight = "BOLD"

def italic():
    global font_slant
    _font_slant = "italic"

def normal():
    global _font_weight, _font_slant
    _font_weight = "normal"
    _font_slant = "roman"

def setfont(s):
    global _font_family
    _font_family = s

# Draw a text string at the given point.                                           
def text(s, x, y):
    global canvas, _font_family, _font_size, _font_weight, _font_slant
    canvas.create_text(x, y, text=s, anchor=SW, fill=_fillcol,  font=(_font_family,_font_size, _font_weight+" "+_font_slant))


def quad (x0,y0, x1,y1, x2,y2, x3,y3):
    global canvas, _fillcol
    canvas.create_polygon (x0,y0, x1,y1, x2,y2, x3,y3, fill=_fillcol, tags='_P')

def strokeweight(s):
    global _linewidth
    _linewidth = s

def arc (x0, y0, x1, y1, start, angle, s=ARC):
    global canvas  # Options are: PIESLICE, ARC, CHORD
    canvas.create_arc(x0, y0, x1, y1, start=start, extent=angle, fill=_fillcol, outline=_strokecol, style=s)

def cvtColor (z):    # Convert an integer to a color (grey)
    return '#%02x%02x%02x' % (z, z, z)  # set your favourite rgb color

def cvtColor3 (r,g,b):
    x = '#%02x%02x%02x' % (r, g, b)
    return x

def rectmode (z):
    global _RECTMODE
    _RECTMODE = z

def background2(bgcol):
    global canvas, width, height
#    canvas.delete('_P')
    canvas.create_rectangle(0, 0 , width+1, height+1, fill=cvtColor(bgcol), tags='_P')

def background(r,g=1000,b=1000):
    global canvas, width, height
    canvas.delete('_P')
    if g == 1000:
        canvas.create_rectangle(0, 0, width+1, height+1, fill=cvtColor3(r, r, r), tags='_P')
    else:
        canvas.create_rectangle(0, 0, width+1, height+1, fill=cvtColor3(r, g, b), tags='_P')

def textsize(n):
    global _font_family, _font_size, _font_weight, _font_slant, font
    _font_size = n
    font = (_font_family, _font_size)

# Image related ---------------------------------------------

def loadImage(s):
    global canvas
    myImage = PhotoImage(file=s)
    return myImage

def image(im, x, y):
    global canvas
    canvas.create_image(x, y, image=im, anchor=NW)

def copyImage (x):
	return x.copy()

def getpixel (im, i, j):
    c = im.get(i,j)
    x = '#%02x%02x%02x' % (c[0], c[1], c[2])
    return x

def setpixel (im, i, j, c):
	return im.put(c, to=(i,j))

def grey (c):
    try:
        g = (c[0]+c[1]+c[2])//3
    except TypeError:
        g = (red(c)+green(c)+blue(c))/3
    return g

def red (c):
    try:
        g = c[0]//1
    except TypeError:
        s = c[1:3]
        g = int(s, base=16)
    return g

def green (c):
    try:
        g = c[1]//1
    except TypeError:
        s = c[3:5]
        g = int(s, base=16)
    return g

def blue (c):
    try:
        g = c[2]//1
    except TypeError:
        s = c[5:]
        g = int(s, base=16)
    return g

def save (im, s):
    im.write(s)

def imageSize(s):
    start(12, 12)
    myImage = PhotoImage(file=s)
    z = (myImage.width(), myImage.height())
    end()
    return z

def start(xs=width, ys=height):
    global width, height, canvas, tkMaster
    tkMaster = Tk()
    canvas = Canvas(tkMaster, width=xs, height=ys)
    canvas.pack()

def end ():
    tkMaster.destroy()
    
def startdraw(xs=width, ys=height):
    global width, height, canvas, tkMaster
    width = xs
    height = ys
    tkMaster = Tk()
    canvas = Canvas(tkMaster, width=xs, height=ys)
    canvas.pack()
    tkMaster.title("Glib tkinter")
    font = ("Helvetica", "12")
    ellipsemode(CENTER)
    rectmode(CORNER)
    background(200)   # Initial empty window

def enddraw():
    mainloop()
