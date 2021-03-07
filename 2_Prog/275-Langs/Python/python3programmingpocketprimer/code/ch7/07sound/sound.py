import pygame
import pygame.mixer
import random

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
sound = pygame.mixer.Sound ("sound.wav")
sound.play()
surf = pygame.display.set_mode((400, 400), pygame.SRCALPHA)
surf.fill ((255,255,255))

while True:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            p = pygame.mouse.get_pos()
    surf.fill ((random.randint(0,255),random.randint(0,255),255))
    pygame.draw.rect (surf, (0,0,200), (100,100,200,30))
    pygame.display.update()
