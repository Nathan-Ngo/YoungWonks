import pygame
from pygame.locals import *
import time
import random
pygame.init()
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
darkgreen = (0,102,0)
aqua = (51,255,255)
yellow = (255,255,0)
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Flappy Bird")
BirdX = 320
BirdY = 240
TopTowerHeight = random.randint(100,200)
##BasicLowerTowerHeight = random.randint(100,200)
##TrueLowerTowerHeight = -BasicLowerTowerHeight
TrueLowerTowerHeight = TopTowerHeight + 150
TowerX = 500
Score = 0
img = pygame.image.load("HeyWeDidItWeTimeTraveledToAlabama.jpg")
def Text(msg,x,y,color):
    fontobj = pygame.font.SysFont("freesans",32)
    msobj = fontobj.render(msg,False,color)
    screen.blit(msobj,(x,y))
while True:
    BirdY += 1
    TowerX -= 1
    screen.blit(img,(0,0))
    pygame.draw.circle(screen,darkgreen,(BirdX,BirdY),30,0)
    pygame.draw.rect(screen,blue,(TowerX,0,50,TopTowerHeight),0)
    pygame.draw.rect(screen,blue,(TowerX,TrueLowerTowerHeight,50,480-TrueLowerTowerHeight),0)
    Text(str(Score),0,0,black)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_w:
                BirdY -= 50
    if TowerX == 0:
            TopTowerHeight  = random.randint(100,200)
            TrueLowerTowerHeight = TopTowerHeight + 150
            TowerX = 500
            Score += 1
            pygame.display.update()
    if BirdX == TowerX and (BirdY <= TopTowerHeight or BirdY >= TrueLowerTowerHeight):
        screen.fill(black)
        Text("Game Over!",215,240,white)
        pygame.display.update()
        break
    if Score > 10:
        screen.fill(black)
        Text('You win!',215,240,white)
        break
    if BirdY + 30 >= 480:
        screen.fill(black)
        Text("Game Over!",215,240,white)
        pygame.display.update()
        break
    if BirdY - 30 <= 0:
        screen.fill(black)
        Text("Game Over!",215,240,white)
        pygame.display.update()
        break
