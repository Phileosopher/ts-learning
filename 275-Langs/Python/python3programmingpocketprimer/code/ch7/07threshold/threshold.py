import pygame
pygame.init()

im = pygame.image.load ("charlie.gif")
width = im.get_width()
height = im.get_height()

for i in range (0,width):
    for j in range(0,height):
        pix = im.get_at ((i,j))
        grey = (pix[0]+pix[1]+pix[2])/3
        if grey < 128:
            im.set_at ((i,j), (0,0,0))
        else:
            im.set_at ((i,j), (255,255,255))

surf = pygame.display.set_mode((width, height), pygame.SRCALPHA)
surf.blit (im, (0,0))
pygame.display.update()
input()
