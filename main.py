import types
import logic_manager
import pygame
from pygame import QUIT
from sys import exit

pygame.init() #begins pygame

dipay = pygame.display

dipay.set_caption('  pygame_chain')

width = 800
hite = 400

see_recpticle = dipay.set_mode((width, hite))

def image_make(imagePath) :
    return pygame.image.load(imagePath).convert_alpha()


frameMaxim = pygame.time.Clock()

font = pygame.font.Font('Pixeltype.ttf' , 20)

testOnTheSeal = image_make('seal.jpeg')

ground = image_make('ground.png')
sky = image_make('Sky.png')


sprite = logic_manager.Sprite(see_recpticle)

frame = 0

testX = 0

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()

    testX += 1

    if testX > 800 :
        testX = 0

    see_recpticle.blit(ground, (0, 300))
    see_recpticle.blit(sky, (0, 0))
    see_recpticle.blit(testOnTheSeal, (testX, 180))


    frame += 1
    dipay.update()
    frameMaxim.tick(60)