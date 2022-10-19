import pygame
from pygame import QUIT
from sys import exit

pygame.init() #begins pygame

dipay = pygame.display

dipay.set_caption('pygame_chain')

frameMaxim = pygame.time.Clock()

Babys_first_surface = pygame.Surface((100,200))

width = 1600
hite = 800

see_recpticle = dipay.set_mode((width, hite))

Babys_first_surface.fill('Red')

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()

    see_recpticle.blit(Babys_first_surface,())

    dipay.update()
    frameMaxim.tick(60)