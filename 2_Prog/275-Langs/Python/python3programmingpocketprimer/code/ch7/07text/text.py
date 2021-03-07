import pygame

width = 400
height = 400
surf = pygame.display.set_mode((width, height),
                        pygame.SRCALPHA)
surf.fill ((255,255,255))
s1 = pygame.Surface((200,200))  # S1 is 200x200
s1.fill ((255,255,255))         # White background
pygame.draw.rect (s1, (230,230, 0), (50, 50, 100, 100), 1)

s2 = pygame.Surface((200,200))  #s2 is also 200x200 pixels
s2.fill ((255,255,255))         # White background too
pygame.draw.circle (s2, (0,200, 50), (60, 60), 50)

# Blit rectangle to (0,0) and circle to (100,100)
surf.blit (s1, (0,0))
surf.blit (s2, (100,100)) # s2 has a circle: blit  pygame.display.update()

pygame.init()
f = pygame.font.Font(None, 30)
text = f.render("Hello There", 1, (10, 10, 10))
surf.blit (text, (100,100))

pygame.display.update()
input()
