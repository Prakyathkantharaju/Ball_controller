import numpy as np
import time
import cv2
import RPi.GPIO as GPIO
from boundary import boundary
from ball_position import ball_position
from motor import motor


bond = boundary()
ball = ball_position()
cap = cv2.VideoCapture(0)
mot = motor()
prev_error_x = 0
prev_error_y = 0
mot.run_motor()
counter_ = 0
while(1):
    time.sleep(0.1)
    counter_ += 1
    _, frame = cap.read()
    # get the center position using the edges using blue filter.
    bond.set_frame(frame)
    wall_boundaries = bond.get_boundaries()
    frame_center = bond.get_center()
    # get the ball position from thresholding.
    ball.set_frame(frame, wall_boundaries)
    ball_present, ball_pos = ball.get_center()
    # Calculate the error from the ball position and center position.
    # print(ball_pos, 'ball')
    # print(frame_center, 'frame')
    error_x = ball_pos[0] - frame_center[0]
    error_y = ball_pos[1] - frame_center[1]
    # print(error_x,error_y)
    ball.vis(ball = True)

    p_planta_dorsi = 0.5
    d_planta_dorsi = 0.001

    p_inversi_eversi = 0.5
    d_inversi_eversi = 0.001
    # error_x = 40
    # error_y = 40
    # NO control window (depends on the camera res)
    if  not(-20 < error_x < 20 and -4 < error_y < 40) and counter_ % 5 == 0 :
        print('in controller x error: ', error_x, 'error y: ', error_y)
    # Calculate the inversion and eversion angle ( - is dorsi)
        planta_dorsi = p_planta_dorsi * error_x + d_planta_dorsi * (error_x - prev_error_x)
        mot.planta_dorsi(abs(planta_dorsi), np.sign(planta_dorsi))
    # Calculate the planta and dorsi angle (+ is inversion)
        inver_evers = p_inversi_eversi * error_y +  d_inversi_eversi * (error_y - prev_error_y)
        mot.inversion_eversion(abs(inver_evers), np.sign(inver_evers))
        mot.run_motor()

    prev_error_x = error_x
    prev_error_y = error_y
    # set motor position
    # mot.run_motor()
    k = cv2.waitKey(5) & 0xFF == ord('q')
    if k:
        break



# Calculate the individual motor torque.



# apply the torque.