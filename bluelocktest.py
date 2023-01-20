import random
import pygame
pygame.init()

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
print("\nPlayer One:",player1.name,"\nStats:\nShooting:",player1.shot,"  Passing:",
player1.passing,"\nDribble: ",player1.dribble,"  Speed:  ",player1.speed)

player2 = Player(playername[player2],playerstats[player2][:2],
playerstats[player2][2:4],playerstats[player2][4:6],playerstats[player2][6:])
print("\nPlayer One:",player2.name,"\nStats:\nShooting:",player2.shot,"  Passing:",
player2.passing,"\nDribble: ",player2.dribble,"  Speed:  ",player2.speed)

player3 = Player(playername[player3],playerstats[player3][:2],
playerstats[player3][2:4],playerstats[player3][4:6],playerstats[player3][6:])
print("\nPlayer One:",player3.name,"\nStats:\nShooting:",player3.shot,"  Passing:",
player3.passing,"\nDribble: ",player3.dribble,"  Speed:  ",player3.speed)