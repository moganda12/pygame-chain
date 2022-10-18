import pygame
from pygame import QUIT
from sys import exit

pygame.init() #begins pygame

dipay = pygame.display

width = 800
hite = 400

see_recpticle = dipay.set_mode((width, hite))

while True:
    for event in pygame.event.get() :
        if event == pygame.QUIT :
            pygame.quit()
            exit()

    dipay.update()