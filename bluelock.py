import random
import pygame
import sys

width = 400
height = 650
grass_color = (121,222,131)
done = False

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(grass_color)

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #goals
        pygame.draw.rect(screen, (255, 255, 255), (150, 0, 100, 25), )
        pygame.draw.rect(screen, (255, 255, 255), (150, 625, 100, 25), )

        #field outline
        pygame.draw.rect(screen, (255, 255, 255), (0, 25, 400, 600), 1)

        #gray corners
        pygame.draw.rect(screen, (172, 172, 172), (0, 0, 150, 25), )
        pygame.draw.rect(screen, (172, 172, 172), (250, 0, 150, 25), )
        pygame.draw.rect(screen, (172, 172, 172), (0, 625, 150, 25), )
        pygame.draw.rect(screen, (172, 172, 172), (250, 625, 150, 25), )

        #black goal outlines
        pygame.draw.lines(screen, (0, 0, 0), False, [(150, 0), (150, 25), (250, 25), (250, 0)], 2)
        pygame.draw.lines(screen, (0, 0, 0), False, [(150, 649), (150, 624), (250, 624), (250, 649)], 2)

        pygame.display.update()
