import random
import pygame
import sys


def main():
    #Sets initial screen values
    pygame.init()
    pygame.display.set_caption('Blue Lock Game')

    global width,height
    width = 800
    height = 650
    grass_color = (121,222,131)

    global font
    font = pygame.font.SysFont("tahoma", 20)

    global screen
    screen = pygame.display.set_mode((width, height))
    screen.fill(grass_color, rect=(0,0,400,650))
    screen.fill((255,255,255), rect=(400,0,400,650))

    global start_img, quit_img
    start_img = pygame.image.load('start.png').convert_alpha()
    quit_img = pygame.image.load('quit.png').convert_alpha()

    global start_button, quit_button
    start_button = Button(650, 50, start_img)
    quit_button = Button(650, 550, quit_img)

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
    pygame.draw.rect(screen, (0, 0, 0), (400, 0, 400, 650), 2)

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

def playerGen(previousnum1,previousnum2):

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
        def __init__(self, name, shot, passing, dribble, speed, usednum):
            self.name = name
            self.shot = shot
            self.passing = passing
            self.dribble = dribble
            self.speed = speed
            self.usednum = usednum

    player1 = random.randint(1,15)
    while player1 == previousnum1 or player1 == previousnum2:
        player1 = random.randint(1,15)

    newplayer = Player(playername[player1],playerstats[player1][:2],
    playerstats[player1][2:4],playerstats[player1][4:6],playerstats[player1][6:],player1)
    return newplayer



def gameLoop(screen):

    done = False
    while done == False:
        #Checks if the return of start_button.draw() == True
        if start_button.draw():
            #replace pass with a function call that starts the game
            player1 = playerGen(0,0)
            text = font.render('Player 1:', True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 120))
            screen.blit(text, text_rect)
            text = font.render(player1.name, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 145))
            screen.blit(text, text_rect)
            text = font.render("Shot: " + player1.shot, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 165))
            screen.blit(text, text_rect)
            text = font.render("Pass: " + player1.passing, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 185))
            screen.blit(text, text_rect)
            text = font.render("Dribble: " + player1.dribble, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 205))
            screen.blit(text, text_rect)
            text = font.render("Speed: " + player1.speed, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 225))
            screen.blit(text, text_rect)
            player2 = playerGen(player1.usednum,0)
            text = font.render('Player 2:', True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 270))
            screen.blit(text, text_rect)
            text = font.render(player2.name, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 295))
            screen.blit(text, text_rect)
            text = font.render("Shot: " + player2.shot, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 315))
            screen.blit(text, text_rect)
            text = font.render("Pass: " + player2.passing, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 335))
            screen.blit(text, text_rect)
            text = font.render("Dribble: " + player2.dribble, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 355))
            screen.blit(text, text_rect)
            text = font.render("Speed: " + player2.speed, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 375))
            screen.blit(text, text_rect)
            player3 = playerGen(player1.usednum,player2.usednum)
            text = font.render('Player 3:', True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 420))
            screen.blit(text, text_rect)
            text = font.render(player3.name, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 445))
            screen.blit(text, text_rect)
            text = font.render("Shot: " + player3.shot, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 465))
            screen.blit(text, text_rect)
            text = font.render("Pass: " + player3.passing, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 485))
            screen.blit(text, text_rect)
            text = font.render("Dribble: " + player3.dribble, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 505))
            screen.blit(text, text_rect)
            text = font.render("Speed: " + player3.speed, True, (0, 0, 0))
            text_rect = text.get_rect(center=(width/1.138, 525))
            screen.blit(text, text_rect)
            pygame.display.update
        #Checks if the return of quit_button.draw() == True
        if quit_button.draw():
            done = True
        for event in pygame.event.get():
            fieldGen(screen)
            if event.type == pygame.QUIT:
                done = True
    

main()
