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
    img = pygame.image.load(imagePath).convert_alpha()
    return img

def collider_make(surf, pos) :
    return surf.get_rect(topleft = pos)

def placeRectBottom(surf, bottomPos) :
    see_recpticle.blit(surf, surf.get_rect(midbottom = bottomPos))

frameMaxim = pygame.time.Clock()

font = pygame.font.Font('Pixeltype.ttf' , 20)

testOnTheSeal = image_make('seal.jpeg')

ground = image_make('ground.png')
groundCollider = collider_make(ground, (0, 300))
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
    placeRectBottom(testOnTheSeal, (testX, 300))


    frame += 1
    dipay.update()
    frameMaxim.tick(60)