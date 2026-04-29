import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

IN1,IN2,IN3,IN4 = 17,27,22,23

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

def stop():
    GPIO.output(IN1,0)
    GPIO.output(IN2,0)
    GPIO.output(IN3,0)
    GPIO.output(IN4,0)

def forward():
    GPIO.output(IN1,1)
    GPIO.output(IN2,0)
    GPIO.output(IN3,1)
    GPIO.output(IN4,0)

def backward():
    GPIO.output(IN1,0)
    GPIO.output(IN2,1)
    GPIO.output(IN3,0)
    GPIO.output(IN4,1)

def left():
    GPIO.output(IN1,0)
    GPIO.output(IN2,1)
    GPIO.output(IN3,1)
    GPIO.output(IN4,0)

def right():
    GPIO.output(IN1,1)
    GPIO.output(IN2,0)
    GPIO.output(IN3,0)
    GPIO.output(IN4,1)

print("f b l r s q")

while True:
    cmd=input("cmd: ")
    if cmd=="f": forward()
    elif cmd=="b": backward()
    elif cmd=="l": left()
    elif cmd=="r": right()
    elif cmd=="s": stop()
    elif cmd=="q": break

GPIO.cleanup()