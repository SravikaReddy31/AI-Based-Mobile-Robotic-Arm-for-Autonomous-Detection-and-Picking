import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pins=[18,19,20,21]

for p in pins:
    GPIO.setup(p,GPIO.OUT)

servos=[GPIO.PWM(p,50) for p in pins]

for s in servos:
    s.start(7)

angles=[60,90,90,90]

def move(i,delta):
    angles[i]=max(10,min(170,angles[i]+delta))
    duty=2+angles[i]/18
    servos[i].ChangeDutyCycle(duty)
    time.sleep(0.3)
    servos[i].ChangeDutyCycle(0)

print("1/2 grip 3/4 shoulder 5/6 base 7/8 joint")

while True:
    c=input("cmd:")
    if c=="1": move(0,-10)
    elif c=="2": move(0,10)
    elif c=="3": move(2,10)
    elif c=="4": move(2,-10)
    elif c=="5": move(3,10)
    elif c=="6": move(3,-10)
    elif c=="7": move(1,10)
    elif c=="8": move(1,-10)
    elif c=="q": break

GPIO.cleanup()