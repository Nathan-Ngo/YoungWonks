
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
##GPIO.setup(

p = GPIO.PWM(26,200)
p.start(50)

while True:
    print('increase')
    for loop in range(1,100,10):
        p.ChangeFrequency(loop)
        time.sleep(1)
    time.sleep(1)
    print('decrease')
    for loop in range(100,1,-10):
        p.ChangeFrequency(loop)
        time.sleep(1)

##p.stop()
