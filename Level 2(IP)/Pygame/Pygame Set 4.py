#Pygame Set 4 Answers
#By Nathan Ngo

#Exercise 1
##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((500,500))
##pygame.display.set_caption("AAAAAA")
##black = (0,0,0)
##white = (255,255,255)
##red = (255,0,0)
##green = (0,255,0)
##blue = (0,0,255)
##Aqua = (0,255,255,128)
##while True:
##    pygame.draw.circle(screen,Aqua,(320,240),30,0)
##    pygame.display.update()
##    screen.fill(black)
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()

#Exercise 2
##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((500,500))
##pygame.display.set_caption("AAAAAA")
##black = (0,0,0)
##white = (255,255,255)
##red = (255,0,0)
##green = (0,255,0)
##blue = (0,0,255)
##Aqua = (0,255,255,128)
##Height = 250
##Width = 250
##while True:
##    Width = Width + 1
##    pygame.draw.circle(screen,Aqua,(Width,Height),30,0)
##    pygame.display.update()
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()

#Exercise 3
##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((500,500))
##pygame.display.set_caption("AAAAAA")
##black = (0,0,0)
##white = (255,255,255)
##red = (255,0,0)
##green = (0,255,0)
##blue = (0,0,255)
##Aqua = (0,255,255,128)
##Height = 250
##Width = 250
##while True:
##    Width = Width + 1
##    pygame.draw.circle(screen,Aqua,(Width,Height),30,0)
##    pygame.display.update()
##    screen.fill(black)
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()

#Exercise 4
##import pygame
##from pygame.locals import *
##pygame.init()
##screen = pygame.display.set_mode((500,500))
##pygame.display.set_caption("Pong!... or at least some of it")
##black = (0,0,0)
##white = (255,255,255)
##red = (255,0,0)
##green = (0,255,0)
##blue = (0,0,255)
##Aqua = (0,255,255,128)
##Height = 250
##Width = 250
##while True:
##    Width = Width + 1
##    pygame.draw.circle(screen,Aqua,(Width,Height),30,0)
##    pygame.display.update()
##    screen.fill(black)
##    if Width == 620:
##        Width = 320
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()

#Exercise 5
##import pygame
##from pygame.locals import *
##import random
##pygame.init()
##screen = pygame.display.set_mode((640,480))
##pygame.display.set_caption("Pong!..., or at least some of it")
##green = (0,255,0)
##black = (0,0,0)
##maroon = (128,0,0)
##teal = (0,0,128)
##CircleX = 320
##CircleY = 240
##XAngleChange = 1
##YAngleChange = 1
##while True:
##    pygame.display.update()
##    screen.fill(black)
##    # draw
##    pygame.draw.circle(screen, green, (CircleX,CircleY), 20,0)
##    # calculate moves
##    CircleY = CircleY + YAngleChange
##    CircleX = CircleX + XAngleChange
##    if CircleX <= -1:
##        XAngleChange = random.randint(1,3)
##    if CircleX >= 621:
##        XAngleChange = random.randint(-3,-1)
##    if CircleY <= -1:
##        YAngleChange = random.randint(1,3)
##    if CircleY >= 461:
##        YAngleChange = random.randint(-3,-1)

#Exercise 6
##import pygame
##from pygame.locals import *
##import random
##pygame.init()
##screen = pygame.display.set_mode((640,480))
##pygame.display.set_caption("Pong!..., or at least some of it")
##green = (0,255,0)
##black = (0,0,0)
##maroon = (128,0,0)
##teal = (0,0,128)
##CircleX = 320
##CircleY = 240
##XAngleChange = 1
##YAngleChange = 1
##while True:
##    pygame.display.update()
##    screen.fill(black)
##    # draw
##    pygame.draw.circle(screen, green, (CircleX,CircleY), 20,0)
##    # events
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    # calculate moves
##    CircleY = CircleY + YAngleChange
##    CircleX = CircleX + XAngleChange
##    if CircleX <= -1:
##        XAngleChange = random.randint(1,3)
##    if CircleX >= 621:
##        XAngleChange = random.randint(-3,-1)
##    if CircleY <= -1:
##        YAngleChange = random.randint(1,3)
##    if CircleY >= 461:
##       YAngleChange = random.randint(-3,-1)

#Exercise 7(Misinterpreted as Exercise 8)
##import pygame
##from pygame.locals import *
##import random
##pygame.init()
##screen = pygame.display.set_mode((640,480))
##pygame.display.set_caption("Pong!..., or at least some of it")
##green = (0,255,0)
##black = (0,0,0)
##maroon = (128,0,0)
##teal = (0,0,128)
##Rectangle1Y = 180
##Rectangle2Y = 180
##RectangleSpeed = 0
##RectangleSpeed2 = 0
##CircleX = 320
##CircleY = 240
##XAngleChange = 1
##YAngleChange = 1
##while True:
##    pygame.display.update()
##    screen.fill(black)
##
##    # draw
##    pygame.draw.rect(screen,maroon,(0,Rectangle1Y,50,100),0)
##    pygame.draw.rect(screen,teal,(590,Rectangle2Y,50,100),0)
##    pygame.draw.circle(screen, green, (CircleX,CircleY), 20,0)
##
##    # events
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##        if event.type == KEYDOWN:
##            if event.key == K_w:
##                RectangleSpeed = -1
##            if event.key == K_s:
##                RectangleSpeed = 1
##            if event.key == K_o:
##                RectangleSpeed2 = -1
##            if event.key == K_l:
##                RectangleSpeed2 = 1
##        if event.type == KEYUP:
##            if event.key == K_w:
##                RectangleSpeed = 0
##            if event.key == K_s:
##                RectangleSpeed = 0
##            if event.key == K_o:
##                RectangleSpeed2 = 0
##            if event.key == K_l:
##                RectangleSpeed2 = 0
##
##    # calculate moves
##    Rectangle1Y += RectangleSpeed
##    Rectangle2Y += RectangleSpeed2
##    CircleY = CircleY + YAngleChange
##    CircleX = CircleX + XAngleChange
##    if Rectangle1Y <= -1:
##        Rectangle1Y = 0
##    if Rectangle1Y >= 381:
##        Rectangle1Y = 380
##    if Rectangle2Y <= -1:
##        Rectangle2Y = 0
##    if Rectangle2Y >= 381:
##        Rectangle2Y = 380
##    if CircleX <= -1:
##        XAngleChange = - XAngleChange
##    if CircleX >= 621:
##        XAngleChange = - XAngleChange
##    if CircleY <= -1:
##        YAngleChange = - YAngleChange
##    if CircleY >= 461:
##        YAngleChange = - YAngleChange

#Exercise 9(Actually is Exercise 8)
##import pygame
##from pygame.locals import *
##import random
##pygame.init()
##screen = pygame.display.set_mode((640,480))
##pygame.display.set_caption("Animation")
##White = (255,255,255)
##Counter = 0
##while True:
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    while Counter <= 50:
##        CircleX = random.randint(0,640)
##        CircleY = random.randint(0,480)
##        pygame.draw.circle(screen,White,(CircleX,CircleY),2,0)
##        pygame.display.update()
##        Counter += 1
##    pygame.display.update()
##CircleX -= 1
##CircleY -= 1

#Exercise 10(Actually is Exercise 9)
import pygame
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Animation")
White = (255,255,255)
black = (0,0,0)
Counter = 0
CircleX = []
CircleY = []
fpsclock = pygame.time.Clock()
def Create():
    CoordinateX = []
    for x in range(0,51,1):
        CoordinateX.append({'x':random.randint(0,640),'y':random.randint(0,480)})
    return CoordinateX

snow = Create()

def Draw(Create):
    for loop_var in Create:
        pygame.draw.circle(screen,White,(loop_var['x'],loop_var['y']),2,0)

def Fall(snow):
    for loop_var in snow:
        loop_var['y'] += 1
        if loop_var['y'] == 480:
            loop_var['y'] = 0
            loop_var['x'] = random.randint(0,640)

while True:
    fpsclock.tick(100)
    pygame.display.update()
    screen.fill(black)
    Draw(snow)
    Fall(snow)
    
#Confusal here!
##while True:
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            pygame.quit()
##            exit()
##    while Counter <= 50:
##        CircleX = random.randint(0,640)
##        CircleY = random.randint(0,480)
##        pygame.draw.circle(screen,White,(CircleX,CircleY),2,0)
##        pygame.display.update()
##        Counter += 1
##CircleX -= 1
##CircleY -= 1
##pygame.display.update()
