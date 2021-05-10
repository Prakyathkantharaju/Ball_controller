import RPi.GPIO as GPIO
import time


class motor(object):
    def __init__(self):
        # start the board
        GPIO.setmode(GPIO.BOARD)
        self.motor_id_list = [0,1,2,3]
        self.motor_pins  = [3,5,19,21]
        self.pwm = []
        self.required_motor = [0,0,0,0]
        #setup pin as 2,3,9,10
        for i,pin in enumerate(self.motor_pins):
            # setting pins as output.
            GPIO.setup(pin, GPIO.OUT)
            # setting up pwm pins into a list: motor
            self.pwm.append(GPIO.PWM(pin, 50))
            self.pwm[-1].start(0)

        

    def _set_angle(self, motor_id, angle, sleep_time = 0.1, switch_off = False):
        #sign convention: 
        # motor 0 +ang -> +height
        # motor 1 +ang -> +height
        # motor 2 -ang -> +height
        # motor 3 -ang -> +height
        for i,j in enumerate(motor_id):
            duty = (angle[i] + 90) / 18 + 2
            print('motor ',i, 'required angle', angle[i]+90, 'duty cycle', duty)
            GPIO.output(self.motor_pins[i], True)
            self.pwm[i].ChangeDutyCycle(duty)
        # controller sleep time
        time.sleep(sleep_time)
        if switch_off:
            for i,j in enumerate(motor_id):
                GPIO.output(self.motor_pins[j], False)

    def planta_dorsi(self, ang, sgn):
        if sgn > 0: # plantar
            # increasing
            self.required_motor[0] += ang
            self.required_motor[2] += ang
            # decreasing
            self.required_motor[1] -= ang
            self.required_motor[3] -= ang
        
        if sgn < 0: # dorsi
            # increasing
            self.required_motor[0] -= ang
            self.required_motor[2] -= ang
            # decreasing
            self.required_motor[1] += ang
            self.required_motor[3] += ang


    def inversion_eversion(self, ang, sgn):
        if sgn > 0: # inversion
            # increasing
            self.required_motor[0] += ang
            self.required_motor[2] += ang
            # decreasing
            self.required_motor[1] += ang
            self.required_motor[3] += ang
        
        if sgn < 0: # eversion
            # increasing
            self.required_motor[0] -= ang
            self.required_motor[2] -= ang
            # decreasing
            self.required_motor[1] -= ang
            self.required_motor[3] -= ang

        
    def run_motor(self, sleep_time = 0):
        self._set_angle(self.motor_id_list, self.required_motor, sleep_time = sleep_time, switch_off = True)