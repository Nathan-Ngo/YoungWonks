#Exercise 1
#Exercise 2
#Exercise 3
#Exercise 4
import pygame
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption(("1/10th of Tic Tac Toe"))
green = (0,255,0)
blue = (0,0,255)
Alpha = False
def X(x,y):
    pygame.draw.line(screen,blue,(x-20,y-20),(x+20,y+20),3)
    pygame.draw.line(screen,blue,(x+20,y-20),(x-20,y+20),3)
pygame.draw.rect(screen,green,(0,0,100,100),0)
while True:
   for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            if x in range(0,50) and y in range(0,50) and Alpha == False:
                X(50,50)
                Alpha = True
            elif x in range(0,50) and y in range(0,50) and Alpha == True:
                pygame.draw.rect(screen,green,(0,0,100,100),0)
                Alpha = False
        pygame.display.update()

#Exercise 5
import pygame
from pygame.locals import *
import random
pygame.init()
screen = pygame.display.set_mode((750,750))
pygame.display.set_caption(("1/10th of Tic Tac Toe"))
green = (0,255,0)
blue = (0,0,255)
Delta = False
def Circle(x,y):
    pygame.draw.circle(screen,blue,(x,y),40,4)
pygame.draw.rect(screen,green,(0,0,100,100),0)
while True:
   for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            if x in range(0,50) and y in range(0,50) and Delta == False:
                Circle(50,50)
                Delta = True
            elif x in range(0,50) and y in range(0,50) and Delta == True:
                pygame.draw.rect(screen,green,(0,0,100,100),0)
                Delta = False
        pygame.display.update()

#Pygame Mini Project 1: Tic Tac Toe
import pygame
from pygame.locals import *
import time
pygame.init()
Alpha = False
Teller = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
white = (255,255,255)
blue = (0,0,255)
black = (0,0,0)
screen = pygame.display.set_mode((750,750))
pygame.display.set_caption("Tic Tac Toe!")
def X(x,y):
    pygame.draw.line(screen,blue,(x-75,y-75),(x+75,y+75),3)
    pygame.draw.line(screen,blue,(x+75,y-75),(x-75,y+75),3)
def Circle(x,y):
    pygame.draw.circle(screen,blue,(x,y),75,1)
while True:
    pygame.draw.line(screen,white,(0,250), (750,250),5)
    pygame.draw.line(screen,white,(0,500), (750,500),5)
    pygame.draw.line(screen,white,(250,0), (250,750),5)
    pygame.draw.line(screen,white,(500,0),(500,750),5)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            if x in range(0,250) and y in range(0,250) and Alpha == False:
                if Teller[1] == '':
                    X(120,120)
                    Teller[1] = 'x'
                    Alpha = True
            elif x in range(0,250) and y in range(0,250) and Alpha == True:
                if Teller[1] == '':
                    Circle(120,120)
                    Teller[1] = 'o'
                    Alpha = False 
            elif x in range(250,500) and y in range(0,250) and Alpha == False:
                if Teller[2] == '':
                    X(370,120)
                    Teller[2] = 'x'
                    Alpha = True
            elif x in range(250,500) and y in range(0,250) and Alpha == True:
                if Teller[2] == '':
                    Circle(370,120)
                    Teller[2] = 'o'
                    Alpha = False 
            elif x in range(500,750) and y in range(0,250) and Alpha == False:
                if Teller[3] == '':
                    X(620,120)
                    Teller[3] = 'x'
                    Alpha = True
            elif x in range(500,750) and y in range(0,250) and Alpha == True:
                if Teller[3] == '':
                    Circle(620,120)
                    Teller[3] = 'o'
                    Alpha = False
            elif x in range(0,250) and y in range(250,500) and Alpha == False:
                if Teller[4] == '':
                    X(120,370)
                    Teller[4] = 'x'
                    Alpha = True
            elif x in range(0,250) and y in range(250,500) and Alpha == True:
                if Teller[4] == '':
                    Circle(120,370)
                    Teller[4] = 'o'
                    Alpha = False
            elif x in range(250,500) and y in range(250,500) and Alpha == False:
                if Teller[5] == '':
                    X(370,370)
                    Teller[5] = 'x'
                    Alpha = True
            elif x in range(250,500) and y in range(250,500) and Alpha == True:
                if Teller[5] == '':
                    Circle(370,370)
                    Teller[5]='o'
                    Alpha = False
            elif x in range(500,750) and y in range(250,500) and Alpha == False:
                if Teller[6] == '':
                    X(620,370)
                    Teller[6] = 'x'
                    Alpha = True
            elif x in range(500,750) and y in range(250,500) and Alpha == True:
                if Teller[6] == '':
                    Circle(620,370)
                    Teller[6] = 'o'
                    Alpha = False
            elif x in range(0,250) and y in range(500,750) and Alpha == False:
                if Teller[7] == '':
                    X(120,620)
                    Teller[7] = 'x'
                    Alpha = True
            elif x in range(0,250) and y in range(500,750) and Alpha == True:
                if Teller[7] == '':
                    Circle(120,620)
                    Teller[7] = 'o'
                    Alpha = False
            elif x in range(250,500) and y in range(500,750) and Alpha == False:
                if Teller[8] == '':
                    X(370,620)
                    Teller = 'x'
                    Alpha = True
            elif x in range(250,500) and y in range(500,750) and Alpha == True:
                if Teller[8] == '':
                    Circle(370,620)
                    Teller = 'o'
                    Alpha = False
            elif x in range(500,750) and y in range(500,750) and Alpha == False:
                if Teller[9] == '':
                    X(620,620)
                    Teller[9] = 'x'
                    Alpha = True
            elif x in range(500,750) and y in range(500,750) and Alpha == True:
                if Teller[9] == '':
                    Circle(620,620)
                    Teller[9] = 'o'
                    Alpha = False
    if Teller[1] == Teller[2] == Teller[3] and Teller[1] != '':
        time.sleep(0.5)
        print(Teller[1],"wins!")
        pygame.display.update()
        break
    if Teller[4] == Teller[5] == Teller[6] and Teller[4] != '':
        time.sleep(0.5)
        print(Teller[4],"wins!")
        pygame.display.update()
        break
    if Teller[7] == Teller[8] == Teller[9] and Teller[7] != '':
        time.sleep(0.5)
        print(Teller[7],"wins!")
        pygame.display.update()
        break
    if Teller[1] == Teller[4] == Teller[7] and Teller[1] != '':
        time.sleep(0.5)
        print(Teller[1],"wins!")
        pygame.display.update()
        break
    if Teller[2] == Teller[5] == Teller[8] and Teller[2] != '':
        time.sleep(0.5)
        print(Teller[2],"wins!")
        pygame.display.update()
        break
    if Teller[3] == Teller[6] == Teller[9] and Teller[3] != '':
        time.sleep(0.5)
        print(Teller[3],"wins!")
        pygame.display.update()
        break
    if Teller[1] == Teller[5] == Teller[9] and Teller[1] != '':
        time.sleep(0.5)
        print(Teller[1],"wins!")
        pygame.display.update()
        break
    if Teller[3] == Teller[5] == Teller[7] and Teller[3] != '':
        time.sleep(0.5)
        print(Teller[1],"wins!")
        pygame.display.update()
        break
        
        
                    



    
