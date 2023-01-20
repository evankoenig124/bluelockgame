import random
import pygame
import sys

width = 400
height = 600
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
        pygame.draw.rect(screen, (255, 255, 255), (100, 550, 200, 50), )
        pygame.display.update()
