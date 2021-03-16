import pygame
from pygame import *
import os
from Lib import inspect
import math

class  Gimage:
    im = None      # Image
    pixels = None  # Pixels data
    w = h = 0
    
    def setIm (self, x):
        self.im = x.convert_alpha()
       # self.im.set_colorkey((255,255,255))
        self.w = self.im.get_size()[0]
        self.h = self.im.get_size()[1]
        self.angle = 0.0

    def alpha (self, a):
        self.im.set_alpha (a)

    def get (self, x, y):
        return self.im.get_at ((x, y))

    def set (self, x, y, c):
        self.im.set_at ((x, y), c)

    def save (self, s):
        pygame.image.save(self.im, (s))

    def rotate (self, a):
        self.angle = a

    def draw (self, canvas, x, y):
    #    canvas.blit( self.im,(x,y) )   # Old
        canvas.blit (self.rot_center(), (x,y))

    def rot_center(self):
        loc = self.im.get_rect().center 
        rot_sprite = pygame.transform.rotate (self.im, self.angle)
        rot_sprite.get_rect().center = loc
        s = rot_sprite.get_size()
        self.w = s[0]
        self.h = s[1]
        return rot_sprite
        
    def copy (self):
        z = Gimage()
        z.setIm (self.im.copy())
        return z
        

_loaded = False
class Gvideo:
    def __init__ (self, name):
        global canvas
        self.name = name
        m = self.loadVideo(name)
        self.vid = m
        self.size = m.get_size()
        self.surf = canvas
        m.set_display(canvas, 
           (0,0,self.size[0], self.size[1]))
        self.outer = canvas
        self.x = 0
        self.y = 0
        self._paused = False
        self.__DEBUG = True
        self.loaded = False

    def loadVideo (self, s):
        global _loaded
        if not _loaded:
            mixer.quit()
            _loaded = True
        try:
            m = movie.Movie (s)
        except:
            print ("Problem loading the movie '", s, "'")
            m = None
        return m 

    def play(self):
        self.vid.play ()

    def locVideo (self, x, y, w, h):
        self.x = x
        self.y = y
        self.size = (w,h)
        self.surf = Surface(self.size)
        self.vid.set_display(self.surf, (0,0,w,h))

    def draw (self):
        global canvas
        canvas.blit (self.surf, (self.x, self.y))

    def copy (self, x, y, w, h):
        inst = Gvideo (self.name)
        inst.locVideo (x, y, w, h)
        return inst

    def stop (self):
        self.vid.stop()

    def rewind (self):
        self.vid.rewind()

    def is_playing (self):
        if self.vid.get_busy(): 
          return True
        return False

    def length (self):
        return self.vid.get_length()

    def where (self):
        if self.vid.get_busy():
            t = self.vid.get_time()
            return t
        else:
            return self.vid.get_length()

    def get_frame (self):       
        return self.surf.copy()

    def pause(self):
        if not self._paused:
            self._paused = True
            fvid = self.vid.get_frame()
            self.vid.pause()
        else:
            self._paused = False
            self.vid.pause()

    def get_frame_number(self):
        return self.vid.get_frame()

    def draw_frame(self, f, iplay=0):
        x = self.vid.render_frame(f)
        if not (self.surf == self.outer):
            x = self.outer.blit (self.surf, (self.x, self.y))
        return
        if iplay == 0:
            self.draw()
        elif iplay == 1:
            self.play()

    def set_frame_number(self, f):
        x = self.vid.render_frame(f)
        if not (self.surf == self.outer):
            x = self.outer.blit (self.surf, (self.x, self.y))
        return
        if iplay == 0:
            self.draw()
        elif iplay == 1:
            self.play()

    def get_pixel(self, x, y):
        if (x<0) or (x>self.size[0]): 
            return (-1, -1, -1)
        if (y<0) or (y>self.size[1]):
            return (-1, -1, -1)
        try:
            p = tuple(self.surf.get_at((x, y)))
        except:
            return (-1, -1, -1)
        return p

    def auto_play (self):
        self.vid.set_display(canvas, 
           (self.x, self.y,self.size[0], self.size[1]))
        self.vid.play()

    def set_volume(self, v):
        return self.vid.set_volume(v)



# To-Do: 1. Symbolic names for special charaters (LEFT, etc)
# These are global variables that are used by the user 
# or are phantoms

K_BACKSPACE  = pygame.K_BACKSPACE
K_TAB        = pygame.K_TAB
K_CLEAR      = pygame.K_CLEAR
K_RETURN     = pygame.K_RETURN
K_PAUSE      = pygame.K_PAUSE
K_ESCAPE     = pygame.K_ESCAPE
K_SPACE      = pygame.K_SPACE
K_EXCLAIM    = pygame.K_EXCLAIM
K_QUOTEDBL   = pygame.K_QUOTEDBL
K_HASH       = pygame.K_HASH
K_DOLLAR     = pygame.K_DOLLAR
K_AMPERSAND  = pygame.K_AMPERSAND
K_QUOTE      = pygame.K_QUOTE       
K_LEFTPAREN  = pygame.K_LEFTPAREN  
K_RIGHTPAREN = pygame.K_RIGHTPAREN
K_ASTERISK   = pygame.K_ASTERISK   
K_PLUS       = pygame.K_PLUS       
K_COMMA      = pygame.K_COMMA      
K_MINUS      = pygame.K_MINUS      
K_PERIOD     = pygame.K_PERIOD     
K_SLASH      = pygame.K_SLASH      
K_0          = pygame.K_0       
K_1          = pygame.K_1       
K_2          = pygame.K_2       
K_3          = pygame.K_3       
K_4          = pygame.K_4       
K_5          = pygame.K_5
K_6          = pygame.K_6       
K_7          = pygame.K_7       
K_8          = pygame.K_8       
K_9          = pygame.K_9       
K_COLON      = pygame.K_COLON
K_SEMICOLON  = pygame.K_SEMICOLON  
K_LESS       = pygame.K_LESS       
K_EQUALS     = pygame.K_EQUALS     
K_GREATER    = pygame.K_GREATER    
K_QUESTION   = pygame.K_QUESTION   
K_AT         = pygame.K_AT         
K_LEFTBRACKET= pygame.K_LEFTBRACKET
K_BACKSLASH  = pygame.K_BACKSLASH  
K_RIGHTBRACKET= pygame.K_RIGHTBRACKET
K_CARET      = pygame.K_CARET      
K_UNDERSCORE = pygame.K_UNDERSCORE 
K_BACKQUOTE  = pygame.K_BACKQUOTE  
#K_a          = pygame.K_a       
K_b          = pygame.K_b       
K_c          = pygame.K_c       
K_d          = pygame.K_d       
K_e          = pygame.K_e       
K_f          = pygame.K_f       
K_g          = pygame.K_g       
K_h          = pygame.K_h       
K_i          = pygame.K_i       
K_j          = pygame.K_j       
K_k          = pygame.K_k       
K_l          = pygame.K_l       
K_m          = pygame.K_m       
K_n          = pygame.K_n       
K_o          = pygame.K_o       
K_p          = pygame.K_p       
K_q          = pygame.K_q       
K_r          = pygame.K_r       
K_s          = pygame.K_s       
K_t          = pygame.K_t       
K_u          = pygame.K_u       
K_v          = pygame.K_v       
K_w          = pygame.K_w       
K_x          = pygame.K_x       
K_y          = pygame.K_y       
K_z          = pygame.K_z       
K_DELETE     = pygame.K_DELETE     
K_KP0        = pygame.K_KP0        
K_KP1        = pygame.K_KP1        
K_KP2        = pygame.K_KP2        
K_KP3        = pygame.K_KP3       
K_KP4        = pygame.K_KP4        
K_KP5        = pygame.K_KP5       
K_KP6        = pygame.K_KP6       
K_KP7        = pygame.K_KP7        
K_KP8        = pygame.K_KP8        
K_KP9        = pygame.K_KP9        
K_KP_PERIOD  = pygame.K_KP_PERIOD  
K_KP_DIVIDE  = pygame.K_KP_DIVIDE  
K_KP_MULTIPLY= pygame.K_KP_MULTIPLY
K_KP_MINUS   = pygame.K_KP_MINUS   
K_KP_PLUS    = pygame.K_KP_PLUS    
K_KP_ENTER   = pygame.K_KP_ENTER   
K_KP_EQUALS  = pygame.K_KP_EQUALS
K_UP         = pygame.K_UP         
K_DOWN       = pygame.K_DOWN       
K_RIGHT      = pygame.K_RIGHT      
K_LEFT       = pygame.K_LEFT       
K_INSERT     = pygame.K_INSERT     
K_HOME       = pygame.K_HOME       
K_END        = pygame.K_END        
K_PAGEUP     = pygame.K_PAGEUP     
K_PAGEDOWN   = pygame.K_PAGEDOWN   
K_F1         = pygame.K_F1
K_F2         = pygame.K_F2
K_F3         = pygame.K_F3
K_F4         = pygame.K_F4
K_F5         = pygame.K_F5
K_F6         = pygame.K_F6
K_F7         = pygame.K_F7
K_F8         = pygame.K_F8
K_F9         = pygame.K_F9
K_F10        = pygame.K_F10
K_F11        = pygame.K_F11
K_F12        = pygame.K_F12
K_F13        = pygame.K_F13
K_F14        = pygame.K_F14
K_F15        = pygame.K_F15
K_NUMLOCK    = pygame.K_NUMLOCK    
K_CAPSLOCK   = pygame.K_CAPSLOCK   
K_SCROLLOCK  = pygame.K_SCROLLOCK  
K_RSHIFT     = pygame.K_RSHIFT     
K_LSHIFT     = pygame.K_LSHIFT     
K_RCTRL      = pygame.K_RCTRL      
K_LCTRL      = pygame.K_LCTRL      
K_RALT       = pygame.K_RALT       
K_LALT       = pygame.K_LALT       
K_RMETA      = pygame.K_RMETA      
K_LMETA      = pygame.K_LMETA      
K_LSUPER     = pygame.K_LSUPER     
K_RSUPER     = pygame.K_RSUPER     
K_MODE       = pygame.K_MODE       
K_HELP       = pygame.K_HELP       
K_PRINT      = pygame.K_PRINT      
K_SYSREQ     = pygame.K_SYSREQ     
K_BREAK      = pygame.K_BREAK      
K_MENU       = pygame.K_MENU       
K_POWER      = pygame.K_POWER      
K_EURO       = pygame.K_EURO
K_A          = 65  
K_B          = 66
K_C          = 67
K_D          = 68
K_E          = 69
K_F          = 70
K_G          = 71
K_H          = 72
K_I          = 73
K_J          = 74
K_K          = 75
K_L          = 76
K_M          = 77
K_N          = 78
K_O          = 79
K_P          = 80
K_Q          = 81
K_R          = 82
K_S          = 83
K_T          = 84
K_U          = 85
K_V          = 86
K_W          = 87
K_X          = 88
K_Y          = 89
K_Z          = 90
mousex = 9                   # X position of the mouse right now
mousey = 10                  # Y position of the mouse right now
_user = None
drawOK = False
_keyp = False
_keyr = False
_mousep = False
_mouser = False
_uppercase = False
_fvid = 0
_xvid = 0
_yvid = 0
_xwid = 0
_ywid = 0
_time = 0
_pausedv = False
savedFrame = None
width = 100                   # Default canvas width
height = 100                  # Default canvas height
_fillcol = (255, 255, 255)    # Current fill color
_strokecol = (0, 0, 0)        # Current stroke color
_bgcol = (200, 200, 200)      # Current background color
_ELLIPSEMODE = 0              # Mode for drawing an ellipse
CENTER = 0                    # 0 = center
RADIUS = 1                    # 1 = radius
CORNER = 2                    # 2 = corner
CORNERS = 3                   # 3 = corners
_RECTMODE = CORNER            # Mode for drawing rectangles

_buttons = (False, False, False)  # Button presses.
key = ""                      # Last key that was pressed
_noloop = False                # Does DRAW loop?
_dofill = True                # Should polygons be filled?
_dostroke = True              # Should polygons be outlined?
_linewidth = 1                # Line width in pixels
_framerate = 30
clock = pygame.time.Clock()
_hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
_font_family = "helvetica"
_font_size = 12
_font_weight = "normal"
_font_slant = "normal"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKSPACE = K_BACKSPACE
PIESLICE = "pieslice"
font = None
canvas = 0

def mouseX():
    return mousex
def mouseY():
    return mousey

def Width():
    global width
    return width
def Height():
    global height
    return height

#  Turn on filling. Set the fill color for polygons,          **
#  text color too.                                            **
def fill(r, g=1000, b=1000, a=255):
    global _fillcol, _dofill
    _dofill = True
    if g==1000:
        _fillcol = (r,r,r,a)
    else:
        _fillcol = (r,g,b,a)
   
# Turn filling off.                                            **
def nofill():
    global _dofill
#    _dofill = False

# Set the line and outline color.                              **
def stroke(r, g=1000, b=1000, a=255):
    global _strokecol, _dostroke
    if g==1000:
        _strokecol=(r,r,r,a)
    else:
        _strokecol=(r,g,b,a)
    _dostroke = True

# Turn off outline drawing.                                    **
def nostroke():
    global _dostroke
    _dostroke = False
    _strokecol = ""

# Set the mode for drawing ellipses.                           **
def ellipsemode (z):
    global _ELLIPSEMODE
    _ELLIPSEMODE = z

# Draw an ellipse. Also used for circles. Four modes as described in doc.           **
def ellipse (xpos, ypos, width, height):
    global canvas, _ELLIPSEMODE
    ccanvas = canvas.copy()
    if _ELLIPSEMODE == CENTER:  # Mode 0 is CENTER
        if _dofill:
            pygame.draw.ellipse (ccanvas, _fillcol, (xpos-width/2, ypos-height/2, width, height), 0)
        if _dostroke:
            if width//2<_linewidth:
                width = _linewidth*2
            if height//2 < _linewidth:
                height = _linewidth*2
            pygame.draw.ellipse (ccanvas, _strokecol, (xpos-width/2, ypos-height/2, width, height), _linewidth)
    elif _ELLIPSEMODE == RADIUS: # Mode 1 is Radius
        if _dofill:
            pygame.draw.ellipse (ccanvas, _fillcol, (xpos-width, ypos-height, width*2, height*2), 0)
        if _dostroke:
            pygame.draw.ellipse (ccanvas, _strokecol, (xpos-width, ypos-height, width*2, height*2), _linewidth)
    elif _ELLIPSEMODE == CORNER:
        if _dofill:
            pygame.draw.ellipse (ccanvas, _fillcol, (xpos, ypos, width, height), 0)
        if _dostroke:
            pygame.draw.ellipse (ccanvas, _strokecol, (xpos, ypos, width, height), _linewidth)
    elif _ELLIPSEMODE == CORNERS:
        if _dofill:
            pygame.draw.ellipse (ccanvas, _fillcol, (xpos, ypos, width-xpos, height-ypos), 0)
        if _dostroke:
            pygame.draw.ellipse (ccanvas, _strokecol, (xpos, ypos, width-xpos, height-ypos), _linewidth)
    else:
        print ("Error: Illegal value for ELLIPSEMODE", _ELLIPSEMODE)  # 101
    ccanvas.set_alpha(_fillcol[3])
    canvas.blit (ccanvas, (0,0))
  
def arc2 (x0, y0, x1, y1, a1, ap, mode="PIESLICE"):
    global canvas, _strokecol, _linewidth, _fillcol
    pygame.draw.arc (canvas, pygame.Rect(x0,y0,x1-x0,y1-y0), a1, ap, _linewidth)

def arc (x0, y0, x1, y1, a1, ap, mode="PIESLICE"):
    global canvas, _strokecol, _linewidth, _fillcol
    ccanvas = canvas.copy()
    conv = 3.1415/180.0
    r = (x1-x0)/2
    xc = x0+r
    yc = y0+r
    xs = x = xc + r*math.cos(-a1*conv)
    ys = y = yc + r*math.sin(-a1*conv)
    xe = xc + r*math.cos(-(a1+ap)*conv)
    ye = yc + r*math.sin(-(a1+ap)*conv)
    a = a1*1.0
    pts = ((x, y),)
    while a <= a1+ap:
        xx = xc + r*math.cos(-a*conv)
        yy = yc + r*math.sin(-a*conv)
        line (x, y, xx, yy)
        pts = pts + ((x, y),)
        x = xx
        y = yy
        a = a + 1
        if (a1+ap)-a<1:
            break
    xx = xc + r*math.cos(-(a1+ap)*conv)
    yy = yc + r*math.sin(-(a1+ap)*conv)
    pts = pts + ((xx, yy),)
    line (x, y, xx, yy)
    x = xx
    y = yy
    if mode == "CHORD":
        line (xe, ye, xs, ys)
        pts = pts + ((xs, ys),)
        pygame.draw.polygon (ccanvas, _fillcol, pts, 0)
        pygame.draw.polygon (ccanvas, _strokecol, pts, _linewidth)                                   
    elif mode == "PIESLICE":
        line (x, y, xc, yc)
        pts = pts + ((xc, yc),)
        line (xc, yc, xs, ys)
        pts = pts + ((xs, ys),)
        pygame.draw.polygon (ccanvas, _fillcol, pts, 0)
        pygame.draw.polygon (ccanvas, _strokecol, pts, _linewidth)
    elif mode == "ARC":
        pygame.draw.polygon (ccanvas, _strokecol, pts, _linewidth)
    ccanvas.set_alpha(_fillcol[3])
    canvas.blit (ccanvas, (0,0))

# Draw a line                                                  **
def line (x0, y0, x1, y1):
    global canvas, _strokecol, _linewidth
    ccanvas = canvas.copy ()
    pygame.draw.line(ccanvas, _strokecol, (x0,y0), (x1,y1), _linewidth)
    ccanvas.set_alpha(_strokecol[3])
    canvas.blit (ccanvas, (0,0))

# Draw a point.                                                **
def point (x, y):
    global _fillcol, canvas
    #ccanvas = canvas.copy()
    ccanvas = pygame.Surface((1,1), 0, 32)
    ccanvas.fill (_fillcol)
   # pygame.draw.line(ccanvas, _fillcol, (x,y), (x,y), 1)
    ccanvas.set_alpha(_fillcol[3])
    canvas.blit (ccanvas, (x,y))

# Draw a rectangle. Same 4 modes as ellipse.                   **
def rect (xpos, ypos, x2, y2):
    global canvas, _RECTMODE
    ccanvas = canvas.copy()
    if _RECTMODE == CENTER:  # Mode 0 is CENTER
        if _dofill:
            pygame.draw.rect (ccanvas, _fillcol, (xpos-x2/2, ypos-y2/2, x2, y2), 0)
        if _dostroke:
            pygame.draw.rect (ccanvas, _strokecol, (xpos-x2/2, ypos-y2/2, x2, y2), _linewidth)
    elif _RECTMODE == RADIUS:      # RADIUS mode
        if _dofill:
            pygame.draw.rect (ccanvas, _fillcol, (xpos-x2, ypos-y2, x2+x2, y2+y2), 0)
        if _dostroke:
            pygame.draw.rect (ccanvas, _strokecol, (xpos-x2, ypos-y2, x2+x2, y2+y2), _linewidth)
    elif _RECTMODE == CORNER:      # CORNER mode
        if _dofill:
            pygame.draw.rect (ccanvas, _fillcol, (xpos, ypos, x2, y2), 0)
        if _dostroke:
            pygame.draw.rect (ccanvas, _strokecol, (xpos, ypos, x2, y2), _linewidth)
    elif _RECTMODE == CORNERS:  #CORNERS
        if _dofill:
            pygame.draw.rect (ccanvas, _fillcol, (xpos, ypos, x2-xpos, y2-ypos), 0)
        if _dostroke:
            pygame.draw.rect (ccanvas, _strokecol, (xpos, ypos, x2-xpos, y2-ypos), _linewidth)
    ccanvas.set_alpha(_fillcol[3])
    canvas.blit (ccanvas, (0,0))
    
# Draw a triangle specified by three points.                   **
def triangle (x0,y0, x1,y1, x2,y2):
    global canvas, _fillcol
    ccanvas = canvas.copy()
    if _dofill:
        pygame.draw.polygon (ccanvas, _fillcol, ((x0,y0), (x1,y1), (x2,y2)), 0)
    if _dostroke:
        pygame.draw.polygon (ccanvas, _strokecol, ((x0,y0), (x1,y1), (x2,y2)), _linewidth)
    ccanvas.set_alpha(_fillcol[3])
    canvas.blit (ccanvas, (0,0))

# Set the frame rate                                           **
def frameRate (r):
    global _framerate
    _framerate = r
    clock.tick(_framerate)
    
def quad (x0,y0, x1,y1, x2,y2, x3,y3):
    global canvas, _fillcol
    ccanvas = canvas.copy()
    canvas.create_polygon (x0,y0, x1,y1, x2,y2, x3,y3, fill=_fillcol, tags='_P')
    ccanvas.set_alpha(_fillcol[3])
    canvas.blit (ccanvas, (0,0))

def strokeweight(s):
    global _linewidth
    _linewidth = s

def cvtColor (z):    # Convert an integer to a color (grey)
      return (z, z, z, 255)

def cvtColor3 (r,g,b, a=255):
      return (r, g, b, a)

def noloop():
    global _noloop
    _noloop = True

def rectmode (z):
    global _RECTMODE
    _RECTMODE = z

def background(r,g=1000,b=1000, a=255):
    global canvas, width, height, _xvid, _yvid, _xwid, _ywid
    ccanvas = canvas.copy()
    if type(r).__name__ == 'tuple':
        f = r
    elif g>=1000:
        f = cvtColor(r)
    else:
        f = cvtColor3(r, g, b)
    ccanvas.fill (f, (0, 0, width, height))
  #  ccanvas.set_alpha(f[3])
    canvas.blit (ccanvas, (0,0))

def setfont(s):
    global _font_family, _font_size, font
    font_family_ = s
    font = pygame.font.SysFont(_font_family, _font_size)

def textsize (n):
    global _font_family, _font_size, _font_weight, _font_slant, font
    _font_size = n
    font = pygame.font.SysFont(_font_family, _font_size)

# Draw a text string at the given point.                       
def text (s, x, y):
    global canvas, font

    if font is None:                   # Create a font if needed
        font = pygame.font.Font(None, 18)
    text = font.render(s, 1, _fillcol) # Render the string in the fill color
    textpos = text.get_rect()   # Get the rectangle that encloses the text
    textpos.bottomleft = [x,y]
    canvas.blit(text, textpos)

def _draw():
    global _user
    global mousex, mousey
    global i,j,canvas, _buttons, mp

    mp = pygame.mouse.get_pos()         # Get mouse coordinates
    mousex = mp[0]
    mousey = mp[1]
    mb = pygame.mouse.get_pressed()     # Get mouse buttons.
    for i in range(0,3):
        if mb[i] and not _buttons[i]:       # Button i pressed.
            _mousePressed(i)
        elif not mb[i] and _buttons[i]:  # Button i released
            _mouseReleased(i)
    _buttons = mb
    if drawOK:
        _user.draw() # Call the user's draw() function if it exists

def _keyPressed (k):
    global _user, _keyp
    if _keyp:
        if len(k)> 0:
            _user.keyPressed(ord(k[0]))

def _keyReleased (k):
    global _user, _keyr
    if _keyr:
        _user.keyReleased (k)

def _mouseReleased (b):
    global _user, _mouser
    if _mouser:
        _user.mouseReleased(b)  # Method exists, and was used.                   

def _mousePressed (b):
    global _user, _mousep
    if _mousep:
        _user.mousePressed(b)



# Equialent of Processing function size, which sets up the display window.
def size (xs, ys):
    global width, height, canvas
    width = xs
    height = ys
    canvas = pygame.display.set_mode( (xs, ys), pygame.DOUBLEBUF, 32)   # Make the sketch window
    pygame.display.set_caption('Drawing')

# ---------------------- Images ---------------------------
def loadImage (s):
    try:
        myImage = pygame.image.load (s)
    except pygame.error:
        return None
    gim = Gimage ()
    gim.setIm (myImage)
    return  (gim)

def image (s, x, y):
    global canvas
    if hasattr(s, "draw"):
        s.draw(canvas, x, y)
    elif hasattr(s, "blit"):
        canvas.blit (s, (x, y))

def get (x, y):
    global canvas
    return tuple(canvas.get_at((x, y)))

def set (x, y, c):
    global canvas 
    canvas.set_at ((x,y), c)

def getpixel (im, x, y):
    return im.get(x,y)

def setpixel (im, i, j, c):
    global canvas
    im.set (i, j, c)

def save(im, s):
    im.save (s)

def imageSize(s):
    try:
        srf = pygame.image.load (s)
    except pygame.error:
        return (0,0)
    return srf.get_size()

def red (c):
    return c[0]
def green(c):
    return c[1]
def blue (c):
    return c[2]

def grey (c):
    return (c[0]+c[1]+c[2])/3

# --------------- Video -----------------------------------
def loadVideo (s):
    try:
        m = Gvideo(s)
    except:
        print ("Problem loading the movie '", s, "'")
        m = None
    print ("LoadVideo type ", type(m))
    return m 

def playVideo (m):
    m.play ()

def autoPlay (m):
    m.auto_play ()

def drawFrame (v, f):
    v.draw_frame(f)

def draw_frame (v, f):
    v.draw_frame(f)

def drawVid (v):
  v.draw()  

def pauseVideo(m):
    m.pause()

def stopVideo (m):
    m.stop()

def rewindVideo (m):
    m.rewind()

def isVideoPlaying (m):
    return m.is_playing()

def setVideoVolume(m, v):
    return m.set_volume(v)

def lengthVideo (m):
    return m.length()

def whereVideo(m):
    return m.where()

def getVideoFrame(m):
    return m.get_frame_number()

def setVideoFrame(m, f):
    m.set_video_frame(f)

def getVideoPixel(m, x, y):
    return m.get_pixel (x, y)

def sizeVideo (m):
    return m.size

def locVideo (m, x, y, w, h):
    global canvas
    if m.surf == canvas:
        m.vid.set_display(canvas, (x,y,w,h))
    else:
        m.locVideo (x,y,w,h)
     

def videoSize (s):
    pygame.init()       
    m = movie.Movie (s)
    x = m.get_size()
    m = None
    return x

# ------------------- Audio --------------------------------
def loadSound (s):
    if mixer.get_init() == False:
        mixer.pre_init(buffersize=512)
        mixer.init()
    try:
        m = mixer.Sound(s)
    except:
        print ("Problem loading the sound file '", s, "'")
        m = None
    return m 

def playSound(a, loop=0):
    a.play(loops=loop)
def stopSound(a):
    a.stop()
def volumeSound (a, v):
    a.set_volume (v)
def durationSound (a):
    return a.get_length()

#def soundData (a):
#    return a.get_raw()
#def playSoundData (a):
#   m = mixer.Sound(buffer=a)
#   m.play()
#  return m
    
    
# --------------------- Interaction ------------------------

def mouse ():
    global mousex, mousex
    mp = pygame.mouse.get_pos() # Get mouse coordinates
    mousex = mp[0]
    mousey = mp[1]
    return mp

def modulename(s):
    for i in range(len(s)-1,0, -1):
        if s[i]=='/' or s[i]=='\\':
            return s[i+1:len(s)-3]

def capture (s):
    pygame.image.save (canvas, s)

def startdraw(w=50, h=50):
    global font, _framerate, clock, _user, drawOK
    global _keyp, _keyr, _mousep, _mouser

    username = inspect.stack()[1][1]  # Get the path of the caller's source
    username = modulename(username)   # extract the file name
    pygame.init()       # Initialize pygame, obviously

    size (w, h)
    ellipsemode(CENTER)
    rectmode (CORNER)
    stroke (0)
    fill (0)
    _user = __import__ (username)  # Import names from user source
    if hasattr (_user, "initialize"):
        if callable(_user.initialize): 
            _user.initialize() # Call the user's SETUP() function if it exists
    if hasattr (_user, "keyPressed"):
        if callable(_user.keyPressed): 
            _keyp = True
    if hasattr (_user, "keyReleased"):
        if callable(_user.keyReleased): 
            _keyr = True
    if hasattr (_user, "mouseReleased"):
        if callable(_user.mouseReleased): 
            _mouser = True
    if hasattr (_user, "mousePressed"):
        if callable(_user.mousePressed): 
            _mousep = True

    background( 200 )   # Initial empty window
 #   ico = loadImage ('c:/pyp/ico/pyp.ico')
 #   pygame.display.set_icon(ico.im)
    pygame.display.set_caption("Glib (Dynamic)")
    font = pygame.font.Font(None, 18)
    clock.tick(_framerate)
    if hasattr (_user, "draw"):
        if callable(_user.draw): 
            drawOK = True

def enddraw():
    global mousex, mousey
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                try:
                    _keyPressed(event.unicode)
                except:
                    continue
            elif event.type == pygame.KEYUP:
                try:
                    _keyReleased(event.key)
                except Exception as e:
                    print ("Problem", e)
                    continue
        if _noloop == False:
            _draw()
            clock.tick(_framerate)
        pygame.display.update()




