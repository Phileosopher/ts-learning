import pygame
pygame.init()
x = 0
y = 100
surf = pygame.display.set_mode((400, 400), pygame.SRCALPHA)
while True:
    surf.fill ((255,255,255))
    pygame.draw.circle (surf, (0,0,200), (x,y), 20)
    x = x + 1
    pygame.display.update()
