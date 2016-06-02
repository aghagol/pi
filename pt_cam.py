import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)

pwm=GPIO.PWM(18,50)
pwm.start(7.5)
sleep(.1)
pwm.stop()

GPIO.cleanup()
# pwm.ChangeDutyCycle(7.5)
