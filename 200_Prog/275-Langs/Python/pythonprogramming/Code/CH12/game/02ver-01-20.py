# Ver 1 - Render initial play area
import Glib

tilesize = 30                # How large (bounding box) is a tile?
ballsize = 10                # How large is the ball?
paddlewidth = 90             # X size of the paddle
paddleheight = 10            # Y size of the paddle
paddley = 420                # Y position of the paddle
paddlex = 180                # Initial X position of the paddle

Glib.startdraw(360, 500)
Glib.fill (100, 100, 240)

for i in range (0, 12):         # Draw top row of tiles
    Glib.ellipse(i*30+15, tilesize*2, 30, 30)
Glib.fill (220, 220, 90)
for i in range (0, 12):         # Draw second row of tiles
    Glib.ellipse(i*30+15, tilesize*3, 30, 30)
Glib.fill (220, 0, 0)
for i in range (0, 12):
    Glib.ellipse(i*30+15, tilesize*4, 30, 30)
Glib.fill (180, 120, 30)
for i in range (0, 12):
    Glib.ellipse(i*30+15, tilesize*5, 30, 30)
Glib.fill (90, 220, 80)
for i in range (0, 12):
    Glib.ellipse(i*30+15, tilesize*6, 30, 30)
Glib.fill (0)
Glib.rect (paddlex, paddley,  paddlewidth, paddleheight)
Glib.enddraw()