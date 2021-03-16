import pygame
pygame.init()
surf = pygame.display.set_mode((400, 400))
c = pygame.Color(0,0,200)
surf.fill ((255,255,255))
y = 60                          # Height at which to start
for n in range (0, 27):         # Draw 30 horizontal blue lines
    for x in range (0,400): # Draw all pixels in one line
        surf.set_at ((x, y),c)  # Draw a blue pixel
    y = y + 20                  # The next line is 20 pixels down
c = (200, 0, 0)                # Pixel color red
for y in range (0, 400):   # Draw connected vertical pixels
    surf.set_at ((25, y), c)    #  to form the margin line
pygame.display.update()
input()
