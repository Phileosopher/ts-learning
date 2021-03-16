import pygame
pygame.init()
clock = pygame.time.Clock()

surf = pygame.display.set_mode((400, 400), pygame.SRCALPHA)
while True:
    clock.tick(30)
    for event in pygame.event.get():
        pass

    surf.fill ((255,255,255))
    pygame.draw.circle (surf, (0,0,200),
                          pygame.mouse.get_pos(), 20)
    pygame.display.update()
