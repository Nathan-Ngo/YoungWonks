import pygame,time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,400))
pygame.display.set_caption("Sprite Animation")
white = (255,255,255)
brown = (139,69,19)
aqua = (0,255,255)
yellow = (255,255,0)

#Image Loading
Jumping = pygame.image.load("Jumping.png")
Jumping2 = pygame.image.load("Jumping2.png")
Jumping3 = pygame.image.load("Jumping3.png")
KirbyTaunt = pygame.image.load("KirbyTaunt.png")
Moving2 = pygame.image.load("Moving2.png")
Moving3 = pygame.image.load("Moving3.png")
Moving4 = pygame.image.load("Moving4.png")
Running = pygame.image.load("Running.png")
Running2 = pygame.image.load("Running2.png")
Standing = pygame.image.load("Standing.png")
Taunt = pygame.image.load("Taunt.png")
Crouch = pygame.image.load("Crouching.png")
Sun = pygame.image.load("Angry Sun.png")
Ground = pygame.image.load("GroundSprite.png")
Cloud = pygame.image.load("Cloud.png")

#Sound Loading


#List Appending
WaddleDeeMoving.append(Moving2)
WaddleDeeMoving.append(Moving3)
WaddleDeeMoving.append(Moving4)
WaddleDeeJumping = []
WaddleDeeJumping.append(Jumping)
WaddleDeeJumping.append(Jumping2)
WaddleDeeJumping.append(Jumping3)
WaddleDeeRunning = []
WaddleDeeRunning.append(Running)
WaddleDeeRunning.append(Running2)
WaddleDeeCrouching = []
WaddleDeeCrouching.append(Crouch)
WaddleDeeKirbyTaunt = []
WaddleDeeKirbyTaunt.append(KirbyTaunt)
WaddleDeeTaunt = []
WaddleDeeTaunt.append(Taunt)

#Variables
Left = 0
Right = 0
Up = 0
Down = 0
MoveHorizontial= 415
MoveVertical = 440
KirbyTaunt = 0
Taunt = 0
RunLeft = 0
RunRight = 0
Sprint = False

#Script
while True:
    pygame.display.update()
    screen.fill(white)
    screen.blit(Ground,(0,0))
    pygame.draw.rect(screen,aqua,(0,0,640,120),0)
    pygame.draw.circle(screen,yellow,(20,20),30,0)
    screen.blit(Cloud,(300,0))
    #Character Moving
    if not Right or not Left or not Up or not Down or not KirbyTaunt:
        screen.blit(Ground,(0,0))
        pygame.draw.rect(screen,aqua,(0,0,640,120),0)
        screen.blit(Sun,(10,10))
        screen.blit(Cloud,(400,0))
        MoveVertical = 100
        screen.blit(Standing,(MoveHorizontial,MoveVertical))
    if Right and Sprint == False:
        for m in WaddleDeeMoving:
            screen.fill(white)
            screen.blit(Ground,(0,0))
            pygame.draw.rect(screen,aqua,(0,0,640,120),0)
            screen.blit(Sun,(10,10))
            screen.blit(Cloud,(400,0))
            screen.blit(m,(MoveHorizontial,MoveVertical))
            pygame.display.update()
            MoveHorizontial += 10
            time.sleep(0.15)
    if Right and Sprint == True:
        for r in WaddleDeeRunning:
            screen.fill(white)
            screen.blit(Ground,(0,0))
            pygame.draw.rect(screen,aqua,(0,0,640,120),0)
            screen.blit(Sun,(10,10))
            screen.blit(Cloud,(400,0))
            screen.blit(r,(MoveHorizontial,MoveVertical))
            pygame.display.update()
            MoveHorizontial += 20
            time.sleep(0.15)
    if Left and Sprint == False:
        for m in WaddleDeeMoving:
            screen.fill(white)
            screen.blit(Ground,(0,0))
            pygame.draw.rect(screen,aqua,(0,0,640,120),0)
            screen.blit(Sun,(10,10))
            screen.blit(Cloud,(400,0))
            m = pygame.transform.flip(m,True,False)
            screen.blit(m,(MoveHorizontial,MoveVertical))
            pygame.display.update()
            MoveHorizontial -= 10
            time.sleep(0.15)
    if Left and Sprint == True:
        for r in WaddleDeeRunning:
            screen.fill(white)
            screen.blit(Ground,(0,0))
            pygame.draw.rect(screen,aqua,(0,0,640,120),0)
            screen.blit(Sun,(10,10))
            screen.blit(Cloud,(400,0))
            r = pygame.transform.flip(r,True,False)
            screen.blit(r,(MoveHorizontial,MoveVertical))
            pygame.display.update()
            MoveHorizontial -= 20
            time.sleep(0.15)
    if Up:
        for j in WaddleDeeJumping:
            screen.fill(white)
            screen.blit(Ground,(0,0))
            pygame.draw.rect(screen,aqua,(0,0,640,120),0)
            screen.blit(Sun,(10,10))
            screen.blit(Cloud,(400,0))
            screen.blit(j,(MoveHorizontial,MoveVertical))
            pygame.display.update()
            MoveVertical -= 10
            time.sleep(0.1)
        for j in WaddleDeeJumping:
            screen.fill(white)
            screen.blit(Ground,(0,0))
            pygame.draw.rect(screen,aqua,(0,0,640,120),0)
            screen.blit(Sun,(10,10))
            screen.blit(Cloud,(400,0))
            screen.blit(j,(MoveHorizontial,MoveVertical))
            pygame.display.update()
            MoveVertical += 10
            time.sleep(0.1)
    if Down:
        for c in WaddleDeeCrouching:
            MoveVertical = MoveVertical + 5
            screen.fill(white)
            screen.blit(Ground,(0,0))
            pygame.draw.rect(screen,aqua,(0,0,640,120),0)
            screen.blit(Sun,(10,10))
            screen.blit(Cloud,(400,0))
            screen.blit(c,(MoveHorizontial,MoveVertical))
            pygame.display.update()
            time.sleep(0.1)
    if KirbyTaunt:
        for k in WaddleDeeKirbyTaunt:
            MoveVertical = MoveVertical - 15
            screen.fill(white)
            screen.blit(Ground,(0,0))
            pygame.draw.rect(screen,aqua,(0,0,640,120),0)
            screen.blit(Sun,(10,10))
            screen.blit(Cloud,(400,0))
            screen.blit(k,(MoveHorizontial,MoveVertical))
            pygame.display.update()
            time.sleep(2)
    if RunLeft:
        for r in WaddleDeeRunning:
            screen.fill(white)
            screen.blit(Ground,(0,0))
            pygame.draw.rect(screen,aqua,(0,0,640,120),0)
            screen.blit(Sun,(10,10))
            screen.blit(Cloud,(400,0))
            r = pygame.transform.flip(r,True,False)
            screen.blit(r,(MoveHorizontial,MoveVertical))
            pygame.display.update()
            MoveHorizontial -= 20
            time.sleep(0.1)
    if RunRight:
        for r in WaddleDeeRunning:
            screen.fill(white)
            screen.blit(Ground,(0,120))
            pygame.draw.rect(screen,aqua,(0,0,640,120),0)
            screen.blit(Sun,(10,10))
            screen.blit(Cloud,(400,0))
            screen.blit(r,(MoveHorizontial,MoveVertical))
            pygame.display.update()
            MoveHorizontial += 20
            time.sleep(0.1)
    if Taunt:
        for a in WaddleDeeTaunt:
            MoveVertical = MoveVertical - 15
            screen.fill(white)
            screen.blit(Ground,(0,0))
            pygame.draw.rect(screen,aqua,(0,0,640,120),0)
            screen.blit(Sun,(10,10))
            screen.blit(Cloud,(400,0))
            screen.blit(a,(MoveHorizontial,MoveVertical))
            pygame.display.update()
            time.sleep(2)
            
        
#Moves
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_d and not Left:
                Right = 1
            if event.key == K_a and not Right:
                Left = 1
            if event.key == K_w and not Down:
                Up = 1
            if event.key == K_s and not Up:
                Down = 1
            if event.key == K_1:
                KirbyTaunt = 1
            if event.key == K_2:
                Taunt = 1
            if event.key == K_c:
                Sprint = True
        if event.type == KEYUP:
            if event.key == K_d:
                Right = 0
            if event.key == K_a:
                Left = 0
            if event.key == K_w:
                Up = 0
            if event.key == K_s:
                Down = 0
            if event.key == K_1:
                KirbyTaunt = 0
            if event.key == K_2:
                Taunt = 0
            if event.key == K_c:
                Sprint = False
#Corner Ending
    if MoveHorizontial >= 621:
        MoveHorizontial = 620
    if MoveHorizontial <= -1:
        MoveHorizontial = 0



