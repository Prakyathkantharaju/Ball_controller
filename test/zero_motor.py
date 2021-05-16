from gpiozero import Servo
from time import sleep

servo = Servo(3, min_pulse_width = 0.15 / 1000, max_pulse_width = 2.75/ 1000)

while True:
    print('min')
    servo.min()
    sleep(1)
    # print('mid')
    # servo.mid()
    # sleep(10)
    print('max')
    servo.max()
    sleep(10)