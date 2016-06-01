import curses

myscreen = curses.initscr()

x = ord('h')

while True:
	myscreen.clear()
	myscreen.border(0)
	myscreen.addstr(12, 25, chr(x))
	myscreen.refresh()
	x = myscreen.getch()
	if chr(x)=='q':
		break

curses.endwin()
