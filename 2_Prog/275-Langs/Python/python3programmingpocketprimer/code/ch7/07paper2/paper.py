import pygame

pygame.init()
y = 60              # Height at which to start
width = 400
height = 400
surf = pygame.display.set_mode((width, height),
                        pygame.SRCALPHA)
surf.fill ((255,255,255))
y = 60                     # Height at which to start
for n in range (0, 27):    # Draw 30 horizontal blue lines
    pygame.draw.line (surf, (0,0,200), (0, y), (width, y))
    y = y + 20             # The next line is 20 pixels down
c = (200, 0, 0)            # Pixel color red
pygame.draw.line (surf, c, (25,0), (25,height))
pygame.display.update()
input()
