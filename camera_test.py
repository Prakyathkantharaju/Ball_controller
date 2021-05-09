import cv2
import cv2.cv2 as cv

cap = cv2.VideoCapture(0)

lower_color_bounds = cv.Scalar(100, 0, 0)
higher_color_bounds = cv.Scalar(225, 80, 80)


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(gray, lower_color_bounds, higher_color_bounds)
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    threshold_frame = frame & mask_bgr
    cv2.imshow('threshold', threshold_frame)

    # Display the resulting frame
    cv2.imshow('rgb', frame)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
