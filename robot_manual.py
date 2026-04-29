import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# motors
IN1,IN2,IN3,IN4=17,27,22,23
for p in [IN1,IN2,IN3,IN4]:
    GPIO.setup(p,GPIO.OUT)

# servos
pins=[18,19,20,21]
for p in pins:
    GPIO.setup(p,GPIO.OUT)

servos=[GPIO.PWM(p,50) for p in pins]
for s in servos: s.start(7)

angles=[60,90,90,90]

def move_servo(i,delta):
    angles[i]=max(10,min(170,angles[i]+delta))
    duty=2+angles[i]/18
    servos[i].ChangeDutyCycle(duty)
    time.sleep(0.3)
    servos[i].ChangeDutyCycle(0)

def forward():
    GPIO.output(IN1,1);GPIO.output(IN2,0)
    GPIO.output(IN3,1);GPIO.output(IN4,0)

def stop():
    GPIO.output(IN1,0);GPIO.output(IN2,0)
    GPIO.output(IN3,0);GPIO.output(IN4,0)

print("Wheels: f b l r s")
print("Arm: 1-8")

while True:
    c=input("cmd:")

    if c=="f": forward()
    elif c=="s": stop()

    elif c=="1": move_servo(0,-10)
    elif c=="2": move_servo(0,10)
    elif c=="3": move_servo(2,10)
    elif c=="4": move_servo(2,-10)
    elif c=="5": move_servo(3,10)
    elif c=="6": move_servo(3,-10)
    elif c=="7": move_servo(1,10)
    elif c=="8": move_servo(1,-10)

GPIO.cleanup()