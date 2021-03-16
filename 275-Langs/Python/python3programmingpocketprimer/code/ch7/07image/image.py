import pygame
pygame.init()

im = pygame.image.load ("charlie.gif")
width = im.get_width()
height = im.get_height()
surf = pygame.display.set_mode((width, height),
                        pygame.SRCALPHA)
surf.fill ((255,255,255))

surf.blit (im, (0,0))
pygame.display.update()
input()
