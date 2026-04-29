import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:

    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Red box
    lower_red = np.array([0,120,70])
    upper_red = np.array([10,255,255])

    # Yellow (double plaster)
    lower_yellow = np.array([10, 80, 80])
    upper_yellow = np.array([35,255,255])

    # White box
    lower_white = np.array([0,0,210])
    upper_white = np.array([180,30,255])

    # Black mouse
    lower_black = np.array([0,0,0])
    upper_black = np.array([180,255,50])

    colors = [
        (lower_red, upper_red, "RED BOX", (0,0,255)),
        (lower_yellow, upper_yellow, "YELLOW OBJECT", (0,255,255)),
        (lower_white, upper_white, "WHITE OBJECT", (255,255,255)),
        (lower_black, upper_black, "BLACK OBJECT", (0,0,0))
    ]

    for lower, upper, name, color in colors:

        mask = cv2.inRange(hsv, lower, upper)
        mask = cv2.GaussianBlur(mask,(5,5),0)
        contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area > 4000:
                x,y,w,h = cv2.boundingRect(cnt)

                cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
                cv2.putText(frame,name,(x,y-10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,color,2)

    cv2.imshow("Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()