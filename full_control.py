import RPi.GPIO as GPIO
import time
import cv2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# MOTOR PINS
IN1,IN2,IN3,IN4 = 17,27,22,23
for p in [IN1,IN2,IN3,IN4]:
    GPIO.setup(p,GPIO.OUT)

# SERVO PINS
pins=[18,19,20,21]
for p in pins:
    GPIO.setup(p,GPIO.OUT)

servos=[GPIO.PWM(p,50) for p in pins]
for s in servos:
    s.start(7)

angles=[60,90,90,90]  # grip, joint, shoulder, base

# MOTOR FUNCTIONS
def forward():
    GPIO.output(IN1,1);GPIO.output(IN2,0)
    GPIO.output(IN3,1);GPIO.output(IN4,0)

def stop():
    GPIO.output(IN1,0);GPIO.output(IN2,0)
    GPIO.output(IN3,0);GPIO.output(IN4,0)

# SERVO FUNCTION
def move_servo(i,angle):
    duty=2+angle/18
    servos[i].ChangeDutyCycle(duty)
    time.sleep(0.4)
    servos[i].ChangeDutyCycle(0)

# PICK AND PLACE
def pick_object():
    print("Picking object...")
    move_servo(2,120)  # shoulder down
    move_servo(0,30)   # close gripper
    move_servo(2,90)   # lift

def drop_object():
    print("Dropping object...")
    move_servo(3,140)  # rotate to box
    move_servo(2,120)  # down
    move_servo(0,90)   # open
    move_servo(2,90)   # up

# MANUAL MODE
def manual():
    print("Manual Mode")
    print("f b l r s")
    print("1-8 arm")

    while True:
        c=input("cmd:")

        if c=="f": forward()
        elif c=="s": stop()

        elif c=="1": move_servo(0,30)
        elif c=="2": move_servo(0,90)
        elif c=="3": move_servo(2,120)
        elif c=="4": move_servo(2,90)
        elif c=="5": move_servo(3,120)
        elif c=="6": move_servo(3,60)
        elif c=="7": move_servo(1,120)
        elif c=="8": move_servo(1,90)

        elif c=="q": break

# AUTOMATIC MODE (COLOR DETECTION)
def automatic():
    print("Automatic Mode Started")

    cap=cv2.VideoCapture(0)

    while True:
        ret,frame=cap.read()
        if not ret: break

        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        # detect BLUE object
        lower=[100,150,0]
        upper=[140,255,255]

        import numpy as np
        mask=cv2.inRange(hsv,np.array(lower),np.array(upper))

        contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        if len(contours)>0:
            c=max(contours,key=cv2.contourArea)

            if cv2.contourArea(c)>2000:
                print("Object detected → moving")
                forward()
                time.sleep(2)
                stop()

                pick_object()
                drop_object()
                break

        cv2.imshow("Camera",frame)

        if cv2.waitKey(1)==27:
            break

    cap.release()
    cv2.destroyAllWindows()

# MAIN
print("1 → Manual")
print("2 → Automatic")

mode=input("Choose: ")

if mode=="1":
    manual()
elif mode=="2":
    automatic()

GPIO.cleanup()