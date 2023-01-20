import random
import pygame
import sys

width = 600
height = 400
grass_color = (121,222,131)
done = False

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(grass_color)

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for x in range(0,)
        pygame.display.update()