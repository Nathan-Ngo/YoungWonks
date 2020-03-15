
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pins = [4,17,18,23]
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins,0)
#4 = LF
#17 = RF
#18 = LB
#23 = RB


def Forward():
    GPIO.output(4,1)
    GPIO.output(17,1)
    GPIO.output(18,0)
    GPIO.output(23,0)
    
def Reverse():
    GPIO.output(18,1)
    GPIO.output(23,1)
    GPIO.output(4,0)
    GPIO.output(17,0)

def Stop():
     GPIO.output(pins,0)
     
def Right():
    GPIO.output(4,1)
    GPIO.output(23,1)
    GPIO.output(17,0)
    GPIO.output(18,0)
    time.sleep(0.125)
    Stop()

def Left():
    GPIO.output(17,1)
    GPIO.output(18,1)
    GPIO.output(4,0)
    GPIO.output(23,0)
    time.sleep(0.125)
    Stop()
    
def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
while True:
    print("Hello! My name is Magellan! W is forward, S is backward, A is left, and D is right")
    key = getch()
    getch()
    if key == 'w':
        Forward()
    elif key == 's':
        Reverse()
    elif key == 'a':
        Left() 
    elif key == 'd':
        Right()
    elif key == 'q':
        break
        
GPIO.cleanup()

