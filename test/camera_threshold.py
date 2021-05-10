import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask_green = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))
    mask_red1 = cv2.inRange(hsv, (0, 70, 50), (10, 255, 255))
    mask_red2 = cv2.inRange(hsv, (170, 70, 50), (180, 255, 255))
    mask_orange = cv2.inRange(hsv, (10, 100, 20), (25, 255, 255))
    mask_yellow = cv2.inRange(hsv, (21, 39, 64), (40, 255, 255))

    ## slice the red and orange
    imask_red1 = mask_red1>0
    imask_red2 = mask_red2>0
    imask_orange = mask_orange>0
    imask_yellow = mask_yellow>0
    red = np.zeros_like(frame, np.uint8)
    red[imask_red1] = frame[imask_red1]
    red[imask_red2] = frame[imask_red2]
    red[imask_orange] = frame[imask_orange]
    red[imask_yellow] = frame[imask_yellow]

    ## slice the green
    imask_green = mask_green>0
    green = np.zeros_like(frame, np.uint8)
    green[imask_green] = frame[imask_green]

    cv2.imshow('green', green)
    cv2.imshow('red', red)
    cv2.imshow('frame', frame)
    cv2.imshow('gray',gray)


    k = cv2.waitKey(5) & 0xFF == ord('q')
    if k:
        break

cv2.destroyAllWindows()
cap.release()
