import random
import pygame
import sys

width = 400
height = 700
grass_color = (121,222,131)
done = False

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(grass_color)

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        pygame.draw.rect(screen, (255, 255, 255), (100, 0, 200, 50), )
        pygame.draw.rect(screen, (255, 255, 255), (100, 650, 200, 50), )
        pygame.draw.rect(screen, (255, 255, 255), (0, 50, 400, 600), 2)
        pygame.display.update()
