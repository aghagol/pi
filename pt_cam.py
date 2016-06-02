import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(24,GPIO.OUT)

pwm=GPIO.PWM(24,50)

pwm.start(7.5)

# pwm.ChangeDutyCycle(7.5)