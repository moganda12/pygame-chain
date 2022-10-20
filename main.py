import logic_manager
import pygame
from pygame import QUIT
from sys import exit

pygame.init() #begins pygame

dipay = pygame.display

dipay.set_caption('pygame_chain')

frameMaxim = pygame.time.Clock()

font = pygame.font.Font('Pixeltype.ttf' , 20)

ground = pygame.image.load('ground.png')
sky = pygame.image.load('Sky.png')

width = 800
hite = 400

see_recpticle = dipay.set_mode((width, hite))

sprite = logic_manager.Sprite(see_recpticle)

frame = 0

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()

    see_recpticle.blit(ground, (0, 300))
    see_recpticle.blit(sky, (0, 0))

    sprite.update
    frame += 1
    dipay.update()
    frameMaxim.tick(60)