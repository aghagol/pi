import curses

myscreen = curses.initscr()

x = ord('s')

while x!=ord('q'):
	myscreen.clear()
	myscreen.border(0)
	myscreen.addstr(12, 25, chr(x))
	myscreen.refresh()
	x = myscreen.getch()

curses.endwin()
