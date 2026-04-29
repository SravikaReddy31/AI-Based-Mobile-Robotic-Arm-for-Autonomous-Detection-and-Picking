import cv2
import serial
import time

# connect NodeMCU
ser = serial.Serial('COM4',9600)
time.sleep(2)

# open USB webcam
cap = cv2.VideoCapture(1)

print("Manual Control Started")
print("f = forward")
print("b = backward")
print("l = left")
print("r = right")
print("s = stop")
print("q = quit")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Robot Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('f'):
        ser.write(b'F')
        print("Forward")

    elif key == ord('b'):
        ser.write(b'B')
        print("Backward")

    elif key == ord('l'):
        ser.write(b'L')
        print("Left")

    elif key == ord('r'):
        ser.write(b'R')
        print("Right")

    elif key == ord('s'):
        ser.write(b'S')
        print("Stop")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()