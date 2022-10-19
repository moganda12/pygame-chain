import logic_manager
import pygame
from pygame import QUIT
from sys import exit

pygame.init() #begins pygame

dipay = pygame.display

dipay.set_caption('pygame_chain')

frameMaxim = pygame.time.Clock()

font = pygame.font.Font('Pixeltype.ttf' , 20)

Babys_first_surface = pygame.Surface((100,200))
image_surface = pygame.image.load('seal.jpeg')
text_suface = font.render('n0o', False, 'Green')

width = 1100
hite = 550

see_recpticle = dipay.set_mode((width, hite))

Babys_first_surface.fill('Red')

frame = 0

while True:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()

    if frame == 0 :
        logic_manager.Sprite.show(Babys_first_surface, (0,0))
        logic_manager.Sprite.show(image_surface, (100, 0))
        logic_manager.Sprite.show(text_suface, (280, 0))

    frame += 1
    dipay.update()
    frameMaxim.tick(60)