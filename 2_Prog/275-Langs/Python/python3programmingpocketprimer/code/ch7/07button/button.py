import pygame
pygame.init()
clock = pygame.time.Clock()
red = 255
surf = pygame.display.set_mode((400, 400), pygame.SRCALPHA)
while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            p = pygame.mouse.get_pos()
            if p[0]>100 and p[0]<200 and p[1]>100 and p[1]<130:
                red = 255-red
    surf.fill ((red,255,255))
    pygame.draw.rect (surf, (0,0,200), (100,100,200,30))
    pygame.display.update()
