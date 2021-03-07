# Ver 1 - Render initial play area
import Glib

Glib.startdraw(400, 800)
Glib.fill (100, 100, 240)
for i in range (0, 12):
    Glib.ellipse(i*30+15, 30, 30, 30)
Glib.fill (220, 220, 90)
for i in range (0, 12):
    Glib.ellipse(i*30+15, 60, 30, 30)
Glib.fill (220, 0, 0)
for i in range (0, 12):
    Glib.ellipse(i*30+15, 90, 30, 30)
Glib.fill (180, 120, 30)
for i in range (0, 12):
    Glib.ellipse(i*30+15, 120, 30, 30)
Glib.fill (90, 220, 80)
for i in range (0, 12):
    Glib.ellipse(i*30+15, 150, 30, 30)
Glib.fill (0)
Glib.rect (180, 350,  90, 10)
Glib.enddraw()
