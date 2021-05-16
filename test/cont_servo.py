import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)
p = GPIO.PWM(5, 50)
p.start(5)


p.ChangeDutyCycle(7.5)
for i in range(2,15):
    print('start')
    p.ChangeDutyCycle(1.5)
    time.sleep(5)
    print('end')
    p.ChangeDutyCycle(2.5)
    time.sleep(5)


GPIO.cleanup()