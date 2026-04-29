import cv2
import serial
import time
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

ser = serial.Serial('COM4',9600,timeout=1)
time.sleep(2)

mode = input("Enter mode (m = manual, a = automatic): ")

cap = cv2.VideoCapture(1)

picked = False

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model(frame)

    annotated = results[0].plot()

    cv2.imshow("Robot Camera", annotated)

    key = cv2.waitKey(1) & 0xFF

    # -------- MANUAL MODE --------

    if mode == 'm':

        if key == ord('f'):
            ser.write(b'F')

        elif key == ord('b'):
            ser.write(b'B')

        elif key == ord('l'):
            ser.write(b'L')

        elif key == ord('r'):
            ser.write(b'R')

        elif key == ord('s'):
            ser.write(b'S')

        elif key == ord('q'):
            break

    # -------- AUTOMATIC MODE --------

    if mode == 'a' and not picked:

        for r in results:

            boxes = r.boxes
            names = r.names

            for box in boxes:

                cls = int(box.cls[0])
                label = names[cls]

                if label == "bottle":

                    print("Bottle detected")

                    ser.write(b'F')
                    time.sleep(2)

                    ser.write(b'S')
                    time.sleep(1)

                    ser.write(b'P')
                    time.sleep(4)

                    picked = True

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()