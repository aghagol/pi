# import picamera
import time
import mover
import curses

s = ord('s')

myscreen = curses.initscr()

state = 'stop'
speed_start = 50

while s!=ord('q'):

	myscreen.clear()
	myscreen.border(0)
	myscreen.refresh()
	s = myscreen.getch()

	if chr(s)=='A':
		if state=='forward':
			speed+=20
		else:
			speed=speed_start
		state = 'forward'
		mover.forward(speed)

	if chr(s)=='B':
		if state=='backward':
			speed+=20
		else:
			speed=speed_start
		state = 'backward'
		mover.backward(speed)

	if chr(s)=='C':
		if state=='rotate_right':
			speed+=20
		else:
			speed=speed_start
		state = 'rotate_right'
		mover.rotate_right(speed)

	if chr(s)=='D':
		if state=='rotate_left':
			speed+=20
		else:
			speed=speed_start
		state = 'rotate_left'
		mover.rotate_left(speed)

	if chr(s)==' ':
		mover.stop()

mover.stop()
curses.endwin()
