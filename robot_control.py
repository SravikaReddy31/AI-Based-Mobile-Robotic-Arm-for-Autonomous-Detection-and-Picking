import cv2
import serial
from ultralytics import YOLO
import time

model = YOLO("yolov8n.pt")

ser = serial.Serial('COM4',9600)
time.sleep(2)

cap = cv2.VideoCapture(1)

while True:

    ret, frame = cap.read()

    results = model(frame)

    annotated = results[0].plot()

    cv2.imshow("Robot Camera", annotated)

    detected = False

    for r in results:
        if len(r.boxes) > 0:
            detected = True

    if detected:

        ser.write(b'F')
        time.sleep(2)

        ser.write(b'S')
        time.sleep(1)

        ser.write(b'P')
        time.sleep(3)

        break

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
ser.close()