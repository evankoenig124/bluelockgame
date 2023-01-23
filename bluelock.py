import random
import pygame
import sys


def main():
    #Sets initial screen values
    pygame.init()
    pygame.display.set_caption('Blue Lock Game')
    
    width = 600
    height = 650
    grass_color = (121,222,131)

    global screen
    screen = pygame.display.set_mode((width, height))
    screen.fill(grass_color, rect=(0,0,400,650))
    screen.fill((255,255,255), rect=(400,0,400,650))

    global start_img, quit_img
    start_img = pygame.image.load('start.png').convert_alpha()
    quit_img = pygame.image.load('quit.png').convert_alpha()

    global start_button, quit_button
    start_button = Button(450, 50, start_img)
    quit_button = Button(450, 550, quit_img)

    gameLoop(screen)

    #Need to use events in main function to prevent input delay
    #for event in pygame.event.get():
        #if event.type == pygame:


class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        action = False
        #draws the button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        #get mouse position
        pos = pygame.mouse.get_pos()
        #checks if mouse is on button
        if self.rect.collidepoint(pos):
            #checks if leftclick is pressed, allows it to be clicked only once
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        #allows button to be clicked again later
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
        


def fieldGen(screen):
    #control panel outline
    pygame.draw.rect(screen, (0, 0, 0), (400, 0, 200, 650), 2)

    #goals
    pygame.draw.rect(screen, (255, 255, 255), (150, 0, 100, 25), )
    pygame.draw.rect(screen, (255, 255, 255), (150, 625, 100, 25), )

    #field outline
    pygame.draw.rect(screen, (255, 255, 255), (0, 25, 400, 600), 1)

    #goal boxes
    pygame.draw.rect(screen, (255, 255, 255), (80, 25, 240, 100), 2)
    pygame.draw.rect(screen, (255, 255, 255), (80, 525, 240, 100), 2)

    #halfway line
    pygame.draw.rect(screen, (255, 255, 255), (0, 325, 400, 600), 2)

    #gray corners
    pygame.draw.rect(screen, (172, 172, 172), (0, 0, 150, 25), )
    pygame.draw.rect(screen, (172, 172, 172), (250, 0, 150, 25), )
    pygame.draw.rect(screen, (172, 172, 172), (0, 625, 150, 25), )
    pygame.draw.rect(screen, (172, 172, 172), (250, 625, 150, 25), )

    #black goal outlines
    pygame.draw.lines(screen, (0, 0, 0), False, [(150, 0), (150, 25), (250, 25), (250, 0)], 2)
    pygame.draw.lines(screen, (0, 0, 0), False, [(150, 649), (150, 623), (250, 623), (250, 649)], 2)

    pygame.display.update()


def gameLoop(screen):

    done = False
    while done == False:
        #Checks if the return of start_button.draw() == True
        if start_button.draw():
            #replace pass with a function call that starts the game
            pass
        #Checks if the return of quit_button.draw() == True
        if quit_button.draw():
            done = True
        for event in pygame.event.get():
            fieldGen(screen)
            if event.type == pygame.QUIT:
                done = True
    

main()