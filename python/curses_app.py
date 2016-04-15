#!/usr/bin/env python

from os import system
import curses
import time


def get_param2(prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	#"which coffee are you roasting?"
	input = screen.getstr(2, 36, 24)
	return input


def get_param(prompt_string):
	screen.clear()
	screen.border(0)
	screen.addstr(2, 2, prompt_string)
	screen.refresh()
	input = screen.getstr(10, 10, 60)
	return input

def execute_cmd(cmd_string):
	system("clear")
	a = system(cmd_string)
	print ""
	if a == 0:
		print "Command executed correctly"
	else:
		print "Command terminated with error"
	raw_input("Press enter")
	print ""

x = 0


try:
	while x != ord('4'):
		screen = curses.initscr()
		curses.start_color()
		curses.raw()

		#we want to accept input, so, this should be there.
		#curses.noecho()


		screen.clear()
		screen.border(0)
		screen.addstr(2, 2, "Please enter a number...")
		screen.addstr(4, 4, "1 - Add a user")
		screen.addstr(5, 4, "2 - Restart Apache")
		screen.addstr(6, 4, "3 - Show disk space")
		screen.addstr(7, 4, "4 - Exit")
		screen.addstr(8, 4, "5 - Start log tail")
		screen.addstr(9, 4, "6 - End log tail")

		screen.refresh()

	    #create a new window
		begin_x = 1; begin_y = 20
		height = 10; width = 100
		win = curses.newwin(height, width, begin_y, begin_x)
		win.border(0)
		win.refresh()

		

	    

	    	def start_log():
				count = 0
				# This needs to be thread, perhaps
				while (count < 5):
					count = count + 1
					win.addstr(count + 1, 2, 'looping # %d' % count)
					#win.printw("This is some other thing ... %d" & count)
					time.sleep(1)
					curses.beep()
					win.refresh()
					#win.printw("This is some other tect")

		x = screen.getch()

		if x == ord('1'):
			username = get_param("Enter the username")
			homedir = get_param("Enter the home directory, eg /home/nate")
			groups = get_param("Enter comma-separated groups, eg adm,dialout,cdrom")
			shell = get_param("Enter the shell, eg /bin/bash:")
			curses.endwin()
			execute_cmd("useradd -d " + homedir + " -g 1000 -G " + groups + " -m -s " + shell + " " + username)
		if x == ord('2'):
			curses.endwin()
			execute_cmd("df")
		if x == ord('3'):
			curses.endwin()
			execute_cmd("df -h")
		if x == ord('5'):
			screen.refresh()
			#curses.endwin()
			start_log()
			#curses.endwin()
			#execute_cmd("tail -f /var/log/system.log")
		if x == ord('6'):
			get_param2('Which coffee are you roasting?')
except Exception as e:
	print e
	curses.endwin()


curses.endwin()
