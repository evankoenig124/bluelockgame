import random
import pygame
import sys

done = False
width = 600
height = 400
grass_color = (121,222,131)

pygame.init()
screen = pygame.display.set_mode((width, height))
screen.fill(grass_color)

while done == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()