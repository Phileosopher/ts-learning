import pygame
import pygame.mixer

def draw_flame():
    pass

def draw_lander (x, y):
    global power, landed
    pygame.draw.rect  (surf, (200,200,200), (x, y,20, 20))
    pygame.draw.circle(surf, (250,250,90), (x+10,y-10), 10)
    pygame.draw.line  (surf, (200,200,200), (x+5,y+20), (x+3,y+22))
    pygame.draw.line  (surf, (200,200,200), (x+3,y+22), (x+18,y+22))
    pygame.draw.line  (surf, (200,200,200), (x+18,y+22), (x+15,y+20))
    pygame.draw.line  (surf, (200,200,200), (x+10,y+10), (x-5, y+25))
    pygame.draw.line  (surf, (200,200,200), (x+10,y+10), (x+25, y+25))

    if power:
        draw_flame()

def landed (x, y):
    global im, surf
    if y>311:
        return True
    if y<10:
        return False
    if x<6 or x>374:
        return False
    c1 = surf.get_at ((x+25, y+26))
    c2 = surf.get_at ((x-5, y+26))
    if c1[0] != 0 and c1[0] != 255:
        return True
    if c2[0] != 0 and c2[0] != 255:
        return True
    return False

def text (s, x, y):
    global font
    text = font.render(s, 1, (200,200,0))
    pygame.draw.rect (surf, (0,0,0), (x, y,200, 20))
    surf.blit (text, (x,y))

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
sound = pygame.mixer.Sound ("engine.wav")
font = pygame.font.Font(None, 22)
dx = 0
dy = 0
fuel = 100
power = False
x,y = 200,100
lnd = False
win, lose = False,False
moveleft,moveright = False,False

# Moonscape is 1145 pixels wide by 337 high.
# What is the height of the ground at any X position?

#sound.play()
surf = pygame.display.set_mode((400, 337), pygame.SRCALPHA)
im = pygame.image.load ("moon.png")
while True:
    clock.tick(10)
    if win:
        text ("You Win", 200, 130)
        pygame.display.update()
        continue
    elif lose:
        text ("You Lose", 200, 130)
        pygame.display.update()
        continue
    p = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                power = True
                sound.play()
            if event.key == pygame.K_LEFT:
                moveleft = True
            if event.key == pygame.K_RIGHT:
                moveright = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                power = False
                sound.stop()
            if event.key == pygame.K_LEFT:
                moveleft = False
            if event.key == pygame.K_RIGHT:
                moveright = False

    if moveleft:
        dx = dx - 1
        fuel = fuel - 0.3
    elif moveright:
        dx = dx + 1
        fuel = fuel - 0.3
    if power:
        fuel = fuel - 1
        dy = dy - 0.3
    else:
        dy = dy + 0.5
    x = int(x + dx)
    y = int(y + dy)

    surf.blit (im, (-100,0))
    draw_lander (x,y)
    if fuel < 0:
        surf.fill ((255,0,0))
        lose = True
    text("Fuel:"+str(int(fuel)), 10, 10)

    if landed(x, y):
        if dy < 3:
            win = True
        else:
            lose = True
    text ("Speed: "+str( int(dy*100)//100)+ " height "+str(y), 200, 20)
    pygame.display.update()


