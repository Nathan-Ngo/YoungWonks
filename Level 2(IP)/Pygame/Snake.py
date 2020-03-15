import pygame
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Snake")
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
aqua = (0,255,255)
gray = (128,128,128)
FoodX = (random.randint(0,600)//10) * 10
FoodY = (random.randint(0,600)//10) * 10
SnakeX = (random.randint(0,600)//10) * 10
SnakeY = (random.randint(0,600)//10) * 10
SnakeSize = []
Up = 0
Down = 0
Left = 0
Right = 0
fpsclock = pygame.time.Clock()
Score = 0
speed = 8
def Text(msg,x,y,color):
    fontobj = pygame.font.SysFont('freesans',32)
    msobj = fontobj.render(msg,False,color)
    screen.blit(msobj,(x,y))
while True:

    fpsclock.tick(speed)
    for y in range(0,600,10):
        for x in range(0,600,10):
            pygame.draw.rect(screen,gray,(x,y,10,10),1)
    SnakeSize.insert(0,[SnakeX,SnakeY])
    
    for segment in SnakeSize:
        pygame.draw.rect(screen,green,segment+[10,10])
    pygame.draw.rect(screen,red,(FoodX,FoodY,10,10),0)
    Text(('Score: '+str(Score)),10,10,white)
    SnakeSize.pop()
    pygame.display.update()
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_w and not Down:
                Up = 1
                Down = 0
                Left = 0
                Right = 0
            elif event.key == K_s and not Up:
                Down = 1
                Up = 0
                Left = 0
                Right = 0
            elif event.key == K_a and not Right:
                Left = 1
                Right = 0
                Down = 0
                Up = 0
            elif event.key == K_d and not Left:
                Right = 1
                Left = 0
                Up = 0
                Down = 0

    #Moves
    if Up:
        SnakeY = SnakeY - 10
    if Down:
        SnakeY = SnakeY + 10
    if Left:
        SnakeX = SnakeX - 10
    if Right:
        SnakeX = SnakeX + 10
  
    #Snake Emerging From Other Sides
    if SnakeX <= -10:
        SnakeX = 610
    elif SnakeX >= 610:
        SnakeX = -10
    elif SnakeY <= -10:
        SnakeY = 610
    elif SnakeY >= 610:
        SnakeY = -10
    #Consumption of Food
    if (FoodX,FoodY) == (SnakeX,SnakeY):
        FoodX = (random.randint(0,600)//10) * 10
        FoodY = (random.randint(0,600)//10) * 10
        Score = Score + 1
  
        SnakeSize.insert(0,[SnakeX,SnakeY])
    


    #Game Over
    if [SnakeX,SnakeY] in SnakeSize[2:]:
        screen.fill(white)
        Text("Game Over!",215,240,black)
        break

    #Restart
    if Score == 9:
        speed += 2
        SnakeSize = []
        
        
