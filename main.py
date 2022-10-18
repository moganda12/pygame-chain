import pygame, sys
from pygame import QUIT

pygame.init() #begins pygame

dipay = pygame.display

width = 800
hite = 400

see_recpticle = dipay.set_mode((width, hite))

while True:
    for event in pygame.event.get() :
        if event == pygame.QUIT :
            pygame.quit()

    dipay.update()