import pygame
from pygame.locals import *
import random
import time
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Pong!")
white = (255,255,255)
green = (0,255,0)
black = (0,0,0)
maroon = (128,0,0)
teal = (0,0,128)
Rectangle1X = 0
Rectangle2X = 600
Rectangle1Y = 180
Rectangle2Y = 180
RectangleSpeed = 0
RectangleSpeed2 = 0
CircleX = 320
CircleY = 240
XAngleChange = 1
YAngleChange = 1
Player1Score = 0
Player2Score = 0
def Text(msg,x,y,color):
    fontobj = pygame.font.SysFont('freesans',20)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
def Text2(msg,x,y,color):
    fontobj = pygame.font.SysFont('freesans',32)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
while True:
    pygame.display.update()
    screen.fill(black)

    # draw
    pygame.draw.rect(screen,maroon,(Rectangle1X,Rectangle1Y,40,100),0)
    pygame.draw.rect(screen,teal,(Rectangle2X,Rectangle2Y,40,100),0)
    pygame.draw.circle(screen, green, (CircleX,CircleY), 20,0)
    pygame.draw.line(screen,white,(320,0),(320,640),2)
    Text("Player 1 Score:"+str(Player1Score),0,0,white)
    Text("Player 2 Score:"+str(Player2Score),480,0,white)

    # events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_w:
                RectangleSpeed = -2.5
            if event.key == K_s:
                RectangleSpeed = 2.5
            if event.key == K_o:
                RectangleSpeed2 = -2.5
            if event.key == K_l:
                RectangleSpeed2 = 2.5
        if event.type == KEYUP:
            if event.key == K_w:
                RectangleSpeed = 0
            if event.key == K_s:
                RectangleSpeed = 0
            if event.key == K_o:
                RectangleSpeed2 = 0
            if event.key == K_l:
                RectangleSpeed2 = 0

    # calculate moves
    Rectangle1Y += RectangleSpeed
    Rectangle2Y += RectangleSpeed2
    CircleY = CircleY + YAngleChange
    CircleX = CircleX + XAngleChange
    if CircleX <= -21:
        CircleX = 320
        CircleY = 240
        XAngleChange = -1
        Player2Score += 1
    if CircleX >= 661:
        CircleX = 320
        CircleY = 240
        XAngleChange = 1
        Player1Score += 1
        pygame.display.update()
    if Rectangle1Y <= -1:
        Rectangle1Y = 0
    if Rectangle1Y >= 381:
        Rectangle1Y = 380
    if Rectangle2Y <= -1:
        Rectangle2Y = 0
    if Rectangle2Y >= 381:
        Rectangle2Y = 380
    if CircleY <= -1:
        YAngleChange = random.randint(1,3)
    if CircleY >= 461:
        YAngleChange = random.randint(-3,-1)
    if (CircleX < Rectangle1X+55 and Rectangle1Y <= CircleY <= Rectangle1Y + 100):
        XAngleChange = -XAngleChange
    if (CircleX > Rectangle2X-15 and Rectangle2Y <= CircleY <= Rectangle2Y + 100):
        XAngleChange = -XAngleChange
    if Player1Score == 11:
        screen.fill(black)
        pygame.draw.circle(screen,white,(310,240),125,0)
        pygame.draw.circle(screen,maroon,(310,240),200,50)
        pygame.draw.rect(screen,maroon,(150,220,50,50),0)
        pygame.draw.rect(screen,maroon,(290,80,50,50),0)
        pygame.draw.rect(screen,maroon,(420,220,50,50),0)
        pygame.draw.rect(screen,maroon,(290,350,50,50),0)
        Text2("Player 1 wins!",215,230,maroon)
        Text("Thank you for playing Pong! by Nathan Ngo",100,450,white)
        pygame.display.update()
        time.sleep(5)
        break
    if Player2Score == 11:
        screen.fill(black)
        pygame.draw.circle(screen,white,(310,240),125,0)
        pygame.draw.circle(screen,teal,(310,240),200,50)
        pygame.draw.rect(screen,teal,(150,220,50,50),0)
        pygame.draw.rect(screen,teal,(290,80,50,50),0)
        pygame.draw.rect(screen,teal,(420,220,50,50),0)
        pygame.draw.rect(screen,teal,(290,350,50,50),0)
        Text2("Player 2 wins!",215,230,teal)
        Text("Thank you for playing Pong! by Nathan Ngo",100,450,white)
        pygame.display.update()
        time.sleep(5)
        break

