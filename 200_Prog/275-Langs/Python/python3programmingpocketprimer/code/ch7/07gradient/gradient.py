import pygame
pygame.init()
surf = pygame.display.set_mode((400, 400))
surf.fill ((255,255,255))
blue = 0
delta = 255.0/400
for y in range (0, 400):
    yy = 400-y
    c = (40, 40, blue)
    for x in range(0, 400):
        surf.set_at  ((x, y), c)
    blue = blue + delta
pygame.display.update()
input()
