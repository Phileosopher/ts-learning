# Tile class development step 0
import Glib

class tile():
    def __init__(self, x, y, color, points):
        self.x = x
        self.y = y
        self.color = color
        self.points = points
        self.active = True
        self.size = 30

    def draw(self):
        if self.active:
            Glib.fill (self.color[0], self.color[1], self.color[2])
            Glib.ellipse (self.x, self.y, self.size, self.size)

def draw():
    global tiles
    for k in tiles:
        k.draw()

Glib.startdraw(360, 350)
red = (250, 0, 0)
print (red)
tiles = ()
for i in range (0, 12):
    tiles = tiles + (tile(i*30+15, 90, red, 15),)
Glib.enddraw()