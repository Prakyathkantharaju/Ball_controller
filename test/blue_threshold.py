import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue) 

    shape_frame = np.shape(mask)
    print(shape_frame, type(shape_frame))
    shape_frame = np.array(shape_frame)
    # performing erosion
    kernel = np.ones((5,5),np.uint8)
    mask = cv2.erode(mask, kernel, iterations = 3)
    test_mask_1 = mask[0:int(shape_frame[0]/2),0:int(shape_frame[1]/2)]
    test_mask_2 = mask[int(shape_frame[0]/2):int(shape_frame[0]),0:int(shape_frame[1]/2)]
    test_mask_3 = mask[0:int(shape_frame[0]/2),int(shape_frame[1]/2):int(shape_frame[1])]
    test_mask_4 = mask[int(shape_frame[0]/2):int(shape_frame[0]),int(shape_frame[1]/2):int(shape_frame[1])]
    box_1 = np.where(200 < test_mask_1)
    box_2 = np.where(200 < test_mask_2)
    box_3 = np.where(200 < test_mask_3)
    box_4 = np.where(200 < test_mask_4)
    if len(box_1[1] > 50) :
        print(np.shape(box_1))
        print(np.mean(box_1, axis = 1))
    if len(box_2[1] > 50) :
        print(np.mean(box_2, axis = 1))
    if len(box_3[1] > 50) :
        print(np.mean(box_3, axis = 1))
    if len(box_4[1] > 50) :
        print(np.mean(box_3, axis = 1))

    cv2.imshow('quad1', test_mask_1)
    cv2.imshow('quad4', test_mask_4)
    cv2.imshow('quad2', test_mask_2)
    cv2.imshow('quad3', test_mask_3)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)

    k = cv2.waitKey(5) & 0xFF == ord('q')
    if k:
        break

cv2.destroyAllWindows()
cap.release()
