from gpiozero import PhaseEnableMotor
motor = PhaseEnableMotor(3, 5)
motor.forward()