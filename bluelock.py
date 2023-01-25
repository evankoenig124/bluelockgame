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

    global font
    font = pygame.font.SysFont("tahoma", 10)

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

def playerGen():

    playerstats = {1:'86817071',2:'81879382',
    3:'78808295',4:'92717474',5:'88738484',
    6:'83838383',7:'73827671',8:'90648685',
    9:'60606060',10:'82859085',11:'85849186',
    12:'91828987',13:'83777673',14:'84868680',
    15:'93678588'}

    playername = {1:'Isagi',2:'Bachira',
    3:'Chigiri',4:'Kunigami',5:'Nagi',
    6:'Reo',7:'Niko',8:'Barou',
    9:'Igaguri',10:'Otoya',11:'Yukimiya',
    12:'Rin',13:'Gagamaru',14:'Karasu',
    15:'Shidou'}

    class Player:
        def __init__(self, name, shot, passing, dribble, speed):
            self.name = name
            self.shot = shot
            self.passing = passing
            self.dribble = dribble
            self.speed = speed

    player1 = random.randint(1,15)
    player2 = random.randint(1,15)
    while player2 == player1:
        player2 = random.randint(1,15)
    player3 = random.randint(1,15)
    while player3 == player1 or player3 == player2:
        player3 = random.randint(1,15)

    player1 = Player(playername[player1],playerstats[player1][:2],
    playerstats[player1][2:4],playerstats[player1][4:6],playerstats[player1][6:])
    print("\nPlayer One:",player1.name,"\n\nShooting:",player1.shot,"  Passing:",
    player1.passing,"\nDribble: ",player1.dribble,"  Speed:  ",player1.speed)

    player2 = Player(playername[player2],playerstats[player2][:2],
    playerstats[player2][2:4],playerstats[player2][4:6],playerstats[player2][6:])
    print("\nPlayer Two:",player2.name,"\n\nShooting:",player2.shot,"  Passing:",
    player2.passing,"\nDribble: ",player2.dribble,"  Speed:  ",player2.speed)

    player3 = Player(playername[player3],playerstats[player3][:2],
    playerstats[player3][2:4],playerstats[player3][4:6],playerstats[player3][6:])
    print("\nPlayer Three:",player3.name,"\n\nShooting:",player3.shot,"  Passing:",
    player3.passing,"\nDribble: ",player3.dribble,"  Speed:  ",player3.speed)



def gameLoop(screen):

    done = False
    while done == False:
        #Checks if the return of start_button.draw() == True
        if start_button.draw():
            #replace pass with a function call that starts the game
            text = font.render('Bachira is da goat NC', True, (0, 0, 0))
            screen.blit(text, (425, 25))
            pygame.display.update
        #Checks if the return of quit_button.draw() == True
        if quit_button.draw():
            done = True
        for event in pygame.event.get():
            fieldGen(screen)
            if event.type == pygame.QUIT:
                done = True
    

main()