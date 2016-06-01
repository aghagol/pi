# import picamera
import time
import mover
import curses

s = ord('s')

myscreen = curses.initscr()

state = 'stop'
speed_start = 50
speed_step = 10
speed_turn_bias = 30

while s!=ord('q'):

	myscreen.clear()
	myscreen.border(0)
	myscreen.refresh()
	s = myscreen.getch()

	if chr(s)=='A':

		if state=='forward' and speed<100:
			speed += speed_step
			mover.forward(speed)

		elif state=='backward' and speed>speed_start:
			speed -= speed_step
			mover.backward(speed)

		else:
			speed = speed_start
			state = 'forward'
			mover.forward(speed)

	if chr(s)=='B':

		if state=='backward' and speed<100:
			speed += speed_step
			mover.backward(speed)

		elif state=='forward' and speed>speed_start:
			speed -= speed_step
			mover.forward(speed)

		else:
			speed = speed_start
			state = 'backward'
			mover.backward(speed)

	if chr(s)=='C':

		if state=='rotate_right' and speed<100:
			speed += speed_step
			mover.rotate_right(speed)

		elif state=='rotate_left' and speed>speed_start:
			speed -= speed_step
			mover.rotate_left(speed)

		else:
			speed = speed_start + speed_turn_bias
			state = 'rotate_right'
			mover.rotate_right(speed)

	if chr(s)=='D':

		if state=='rotate_left' and speed<100:
			speed += speed_step
			mover.rotate_left(speed)

		elif state=='rotate_right' and speed>speed_start:
			speed -= speed_step
			mover.rotate_right(speed)

		else:
			speed = speed_start + speed_turn_bias
			state = 'rotate_left'
			mover.rotate_left(speed)

	if chr(s)==' ':
		mover.stop()
		state = 'stop'
		speed = speed_start

mover.stop()
curses.endwin()
