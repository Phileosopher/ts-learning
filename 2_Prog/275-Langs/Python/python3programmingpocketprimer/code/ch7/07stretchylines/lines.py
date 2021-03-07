import pygame
pygame.init()
clock = pygame.time.Clock()
x0,y0 = -1,-1
x1,y1 = -1,-1
surf = pygame.display.set_mode((400, 400), pygame.SRCALPHA)
while True:
    clock.tick(30)
    p = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            x1,y1 = p[0],p[1]
        if event.type == pygame.MOUSEBUTTONDOWN:
            x0,y0 = p[0],p[1]
    surf.fill ((255,255,255))
    if x1 >= 0:
        pygame.draw.line (surf, (0,0,200), (x0,y0),(x1,y1))
    elif x0 >= 0:
        pygame.draw.line (surf, (0,0,200), (x0,y0),(p[0],p[1]))
    pygame.display.update()
