import time
import numpy as np
import cv2
import RPi.GPIO as GPIO


# start the board
GPIO.setmode(GPIO.BOARD)


motor_id_list = [0,1, 2, 3]
motor_pins  = [3,5,19,21]
pwm = []
#setup pin as 2,3,9,10
for i,pin in enumerate(motor_pins):
    print(pin)
    # setting pins as output.
    GPIO.setup(pin, GPIO.OUT)
    # setting up pwm pins into a list: motor
    pwm.append(GPIO.PWM(pin, 50))
    pwm[-1].start(0)


def SetAngle(motor_id, angle, sleep_time = 3):
    for i,j in enumerate(motor_id):
        duty = angle[i] / 18 + 2
        GPIO.output(motor_pins[j], True)
        pwm[j].ChangeDutyCycle(duty)
    time.sleep(sleep_time)
    for i,j in enumerate(motor_id):
        GPIO.output(motor_pins[j], True)
    # pwm[motor_id].ChangeDutyCycle(0)

    

for i in range(10):
   SetAngle([0,1,2,3], [90,90,90,90], 0.1)
# test up and down
for i in range(10):
    SetAngle([0,1,2,3], [150,150,30,30], 0.5)
    SetAngle([0,1,2,3], [40,40,140,140], 0.5)
# 
# SetAngle([0,1,2,3], [90,90,90,90], 0.1)
# time.sleep(10)
# test planta and dorsi (x axis)
for i in range(10):
    # planta
    SetAngle([0,1,2,3], [120,58,120,60], 1)
    SetAngle([0,1,2,3], [60,120,60,120], 1)
# 
SetAngle([0,1,2,3], [90,90,90,90], 0.1)
# test inversion and eversion (y axis)
for i in range(10):
    # inversion
    SetAngle([0,1,2,3], [120,118,120,120], 1)
    SetAngle([0,1,2,3], [60,58,60,60], 1)
SetAngle([0,1,2,3], [90,90,90,90], 0.5)
# 
# # test inversion and eversion (x axis)
# SetAngle([0,1,2,3], [90,90,90,90], 0.5)
# SetAngle(1, 90, 0.5)
# SetAngle(2, 90, 0.5)
# SetAngle(3, 90, 0.5)
# increm = [0,1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0]
# for i in range(len(increm)):
#     print(i)
#     print(90 + (10 * increm[i]))
#     print(90 - (10 * increm[i]))
#     SetAngle(0, 90 + (10 * increm[i]), 0.5)
#     SetAngle(1, 90 - (10 * increm[i]), 0.5)




