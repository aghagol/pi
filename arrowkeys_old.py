import curses

s = ord('s')

x = 1
y = 1

myscreen = curses.initscr()

while s!=ord('q'):
	myscreen.clear()
	myscreen.border(0)
	myscreen.addstr(x, y, 'Move me! (or press \'q\' to quit)')
	myscreen.refresh()
	s = myscreen.getch()
	if chr(s)=='A' and x>0	: x -= 1
	if chr(s)=='B' and x<22	: x += 1
	if chr(s)=='C' and y<55	: y += 1
	if chr(s)=='D' and y>0	: y -= 1

curses.endwin()
