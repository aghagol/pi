import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 19200, timeout = 1)

def forward(speed):
    command_right = chr(0xC6)
    command_left = chr(0xCE)
    ser.write(command_right)
    ser.write(chr(speed))
    ser.write(command_left)
    ser.write(chr(speed))
 
def backward(speed):
    command_right = chr(0xC5)
    command_left = chr(0xCD)
    ser.write(command_right)
    ser.write(chr(speed))
    ser.write(command_left)
    ser.write(chr(speed))
 
def stop():
    command_right = chr(0xC6)
    command_left = chr(0xCE)
    ser.write(command_right)
    ser.write(chr(0))
    ser.write(command_left)
    ser.write(chr(0))
 
def rotate_left(speed):
    command_right = chr(0xC6)
    command_left = chr(0xCD)
    ser.write(command_right)
    ser.write(chr(speed))
    ser.write(command_left)
    ser.write(chr(speed))
 
def rotate_right(speed):
    command_right = chr(0xC5)
    command_left = chr(0xCE)
    ser.write(command_right)
    ser.write(chr(speed))
    ser.write(command_left)
    ser.write(chr(speed))

# forward(95)
# time.sleep(1)
# rotate_right(90)
# time.sleep(1)
# forward(95)
# time.sleep(1)
# backward(95)
# time.sleep(1)
# stop()
