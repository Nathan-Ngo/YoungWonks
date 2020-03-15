#Pygame Set 3 Answers
#By Nathan Ngo

#Exercise 1
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption(" ")
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

#Exercise 2
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
def Menu():
    pygame.display.set_caption("Game")
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

#Exercise 3
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,480))
def Menu():
    pygame.display.set_caption("Game")
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
Menu()

#Exercise 4
import pygame
from pygame.locals import *
pygame.init()
Aqua = (0,255,255)
NavyBlue = (0,0,128)
screen = pygame.display.set_mode((640,480))
pygame.draw.rect(screen,Aqua,(0,0,100,300),0)
pygame.draw.rect(screen,NavyBlue,(400,0,100,300),0)
def Menu():
    pygame.display.set_caption("Game")
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
Menu()

#Exercise 5
import pygame
from pygame.locals import *
pygame.init()
Aqua = (0,255,128)
NavyBlue = (0,0,128)
screen = pygame.display.set_mode((640,480))
pygame.draw.rect(screen,Aqua,(0,0,100,300),0)
pygame.draw.rect(screen,NavyBlue,(400,0,100,300),0)
def show_text(msg,x,y,color):
    fontobj = pygame.font.SysFont("freesans",32)
    msobj = fontobj.render(msg,False,color)
    screen.blit(msobj,(x,y))
def Menu():
    pygame.display.set_caption("Game")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        pygame.display.update()
        
        show_text("Play",0,0,NavyBlue)
        show_text("Quit",100,0,Aqua)
        show_text("Testing, By Nathan Ngo",300,400,NavyBlue)

Menu()

#Exercise 6
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((750,750))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
something  = (0,255,255)
pygame.display.set_caption("weeee")
def show_text(msg,x,y,color):
    fontobj = pygame.font.SysFont("freesans", 32)
    msobj = fontobj.render(msg,False,color)
    screen.blit(msobj,(x,y))
pygame.draw.rect(screen,something,(0,0,375,750),0)
pygame.draw.rect(screen,green,(375,0,475,750),0)
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        exit()
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        x,y = event.pos
        if x in range(0,375) and y in range(0,750):
            print("Play")
        if x in range(375,750) and y in range (0,750):
            print("Quit")
    show_text("Quit", 375,0, red)
    show_text("Play",0,0,green)
pygame.display.update()

#Exercise 7
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((750,600))
red  = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
def show_text(msg,x,y,color):
    fontobj = pygame.font.SysFont("freesans", 32)
    msobj = fontobj.render(msg,False,color)
    screen.blit(msobj,(x,y))
def Menu():
    pygame.display.set_caption("Tic Tac Toe - Menu")
    show_text("Tic Tac Toe!",275,0,white)
    show_text("By Nathan Ngo",275,50,white)
    pygame.draw.rect(screen,white,(275,400,100,50),0)
    show_text("Play",275,400,black)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                if x in range(275,375) and y in range(400,450):
                    TicTacToe()
def TicTacToe():
    import time
    Alpha = False
    Teller = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
    white = (255,255,255)
    blue = (0,0,255)
    black = (0,0,0)
    def X(x,y):
        pygame.draw.line(screen,blue,(x-75,y-75),(x+75,y+75),3)
        pygame.draw.line(screen,blue,(x+75,y-75),(x-75,y+75),3)
    def Circle(x,y):
        pygame.draw.circle(screen,blue,(x,y),75,1)
    screen.fill(black)
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
Menu()

#Exercise 8
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((750,600))
red  = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
def show_text(msg,x,y,color):
    fontobj = pygame.font.SysFont("freesans", 32)
    msobj = fontobj.render(msg,False,color)
    screen.blit(msobj,(x,y))
def Menu():
    pygame.display.set_caption("Tic Tac Toe - Menu")
    show_text("Tic Tac Toe!",275,0,white)
    show_text("By Nathan Ngo",275,50,white)
    pygame.draw.rect(screen,white,(275,400,100,50),0)
    show_text("Play",275,400,black)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                if x in range(275,375) and y in range(400,450):
                    def TicTacToe():
                        import time
                        Alpha = False
                        Teller = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
                        white = (255,255,255)
                        blue = (0,0,255)
                        black = (0,0,0)
                        def X(x,y):
                            pygame.draw.line(screen,blue,(x-75,y-75),(x+75,y+75),3)
                            pygame.draw.line(screen,blue,(x+75,y-75),(x-75,y+75),3)
                        def Circle(x,y):
                            pygame.draw.circle(screen,blue,(x,y),75,1)
                        screen.fill(black)
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
                    TicTacToe()
Menu()

#Exercise 9
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((750,600))
red  = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
def show_text(msg,x,y,color):
    fontobj = pygame.font.SysFont("freesans", 32)
    msobj = fontobj.render(msg,False,color)
    screen.blit(msobj,(x,y))
def Menu():
    pygame.display.set_caption("Tic Tac Toe - Menu")
    show_text("Tic Tac Toe!",275,0,white)
    show_text("By Nathan Ngo",275,50,white)
    pygame.draw.rect(screen,white,(275,400,100,50),0)
    show_text("Play",275,400,black)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x,y = event.pos
                if x in range(275,375) and y in range(400,450):
                    def TicTacToe():
                        import time
                        Alpha = False
                        Teller = {1:'',2:'',3:'',4:'',5:'',6:'',7:'',8:'',9:''}
                        white = (255,255,255)
                        blue = (0,0,255)
                        black = (0,0,0)
                        def X(x,y):
                            pygame.draw.line(screen,blue,(x-75,y-75),(x+75,y+75),3)
                            pygame.draw.line(screen,blue,(x+75,y-75),(x-75,y+75),3)
                        def Circle(x,y):
                            pygame.draw.circle(screen,blue,(x,y),75,1)
                        screen.fill(black)
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
                                time.sleep(5)
                                screen.fill(black)
                                Menu()
                                pygame.display.update()
                            if Teller[4] == Teller[5] == Teller[6] and Teller[4] != '':
                                time.sleep(0.5)
                                print(Teller[4],"wins!")
                                pygame.display.update()
                                time.sleep(5)
                                screen.fill(black)
                                Menu()
                                pygame.display.update()
                            if Teller[7] == Teller[8] == Teller[9] and Teller[7] != '':
                                time.sleep(0.5)
                                print(Teller[7],"wins!")
                                pygame.display.update()
                                time.sleep(5)
                                screen.fill(black)
                                Menu()
                                pygame.display.update()
                            if Teller[1] == Teller[4] == Teller[7] and Teller[1] != '':
                                time.sleep(0.5)
                                print(Teller[1],"wins!")
                                pygame.display.update()
                                time.sleep(5)
                                screen.fill(black)
                                Menu()
                                pygame.display.update()
                            if Teller[2] == Teller[5] == Teller[8] and Teller[2] != '':
                                time.sleep(0.5)
                                print(Teller[2],"wins!")
                                pygame.display.update()
                                break
                            if Teller[3] == Teller[6] == Teller[9] and Teller[3] != '':
                                time.sleep(0.5)
                                print(Teller[3],"wins!")
                                pygame.display.update()
                                time.sleep(5)
                                screen.fill(black)
                                Menu()
                                pygame.display.update()
                            if Teller[1] == Teller[5] == Teller[9] and Teller[1] != '':
                                time.sleep(0.5)
                                print(Teller[1],"wins!")
                                pygame.display.update()
                                time.sleep(5)
                                screen.fill(black)
                                Menu()
                                pygame.display.update()
                            if Teller[3] == Teller[5] == Teller[7] and Teller[3] != '':
                                time.sleep(0.5)
                                print(Teller[1],"wins!")
                                pygame.display.update()
                                time.sleep(5)
                                screen.fill(black)
                                Menu()
                                pygame.display.update()
                    TicTacToe()
Menu()


