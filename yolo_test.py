import cv2
import serial
import time

# change COM port if needed
ser = serial.Serial('COM4',9600)
time.sleep(2)

mode = input("Enter mode (m = manual, a = automatic): ")

# USB webcam
cap = cv2.VideoCapture(1)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        break

    cv2.imshow("Robot Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    # -------- MANUAL MODE --------
    if mode == 'm':

        if key == ord('w'):
            ser.write(b'F')

        elif key == ord('s'):
            ser.write(b'B')

        elif key == ord('a'):
            ser.write(b'L')

        elif key == ord('d'):
            ser.write(b'R')

        elif key == ord('x'):
            ser.write(b'S')

    # -------- AUTOMATIC MODE --------
    elif mode == 'a':

        ser.write(b'F')
        time.sleep(2)

        ser.write(b'L')
        time.sleep(1)

        ser.write(b'R')
        time.sleep(1)

        ser.write(b'S')
        time.sleep(2)

    if key == ord('q'):
        ser.write(b'S')
        break

cap.release()
cv2.destroyAllWindows()
ser.close()