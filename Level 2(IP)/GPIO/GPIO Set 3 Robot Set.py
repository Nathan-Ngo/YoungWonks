
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pins = [4,17,18,23]
GPIO.setup(pins, GPIO.OUT)
GPIO.output(pins,0)
a = GPIO.PWM(4,0)
b = GPIO.PWM(17,0)
c = GPIO.PWM(18,0)
d = GPIO.PWM(23,0)
speed = 50
#4 = LF
#17 = RF
#18 = LB
#23 = RB


def Forward():
    a.start(speed)
    b.start(speed)
    c.stop()
    d.stop()
def Reverse():
    a.stop()
    b.stop()
    c.start(speed)
    d.start(speed)

def Stop():
     a.stop()
     b.stop()
     c.stop()
     d.stop()
     
def Right():
    a.stop()
    b.start(speed)
    c.stop()
    d.start(speed)
    time.sleep(0.125)
    Stop()

def Left():
    a.start(speed)
    b.stop()
    c.start(speed)
    d.stop()
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

