import RPi.GPIO as GPIO
from time import sleep
import numpy as np

GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)

p=GPIO.PWM(16,50)
t=GPIO.PWM(18,50)

p.start(5)
t.start(5)
sleep(.1)

for d in np.arange(5.5,10,.5):
	p.ChangeDutyCycle(d)
	sleep(.1)
p.ChangeDutyCycle(5)

sleep(.1)
for d in np.arange(5.5,10,.5):
	t.ChangeDutyCycle(d)
	sleep(.1)
t.ChangeDutyCycle(5)

p.stop()
t.stop()

GPIO.cleanup()
# pwm.ChangeDutyCycle(7.5)
