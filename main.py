import pygame
from pygame import QUIT
from sys import exit

pygame.init() #begins pygame

dipay = pygame.display

dipay.set_caption('pygame_chain')

width = 800
hite = 400

see_recpticle = dipay.set_mode((width, hite))

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()

    dipay.update()