# import picamera
import time
import mover
import curses

s = ord('s')

myscreen = curses.initscr()

while s!=ord('q'):
	myscreen.clear()
	myscreen.border(0)
	myscreen.refresh()
	s = myscreen.getch()
	if chr(s)=='A':
		mover.forward(55)
		time.sleep(.2)
	if chr(s)=='B':
		mover.backward(55)
		time.sleep(.2)
	if chr(s)=='C':
		mover.rotate_right(55)
		time.sleep(.2)
	if chr(s)=='D':
		mover.rotate_left(55)
		time.sleep(.2)

curses.endwin()
