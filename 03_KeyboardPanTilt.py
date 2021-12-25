#!/usr/bin/env python
# Control the pan and tilt mechanism in 5 degrees angle increments using keyboard arrow keys
# 'q' to quit
import curses
import time
import pantilthat

# Disable servos on timeout. 1/4 second is sufficient to complete a 5 degrees angle adjustment
pantilthat.idle_timeout(0.25)

# Set start up servo positions
p = 0
t = 0
pantilthat.pan(p)
pantilthat.tilt(t)

# Initialize curses and get the screen window
screen = curses.initscr()

# Map arrow keys to special values like KEY_RIGHT, KEY_UP etc.
screen.keypad(True)

# Set up arrow key angle change
deltaAngle = 5

# Main process to read keyboard and act
# Swap 'left' and 'right' processing to switch between SelfieView and FirstPersonView
try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            # if q is pressed quit
            pantilthat.pan(0)
            pantilthat.tilt(0)
            time.sleep(1)            
            break
        elif char == curses.KEY_RIGHT:
            screen.addstr(0, 0, 'right ')
            if (p + deltaAngle) < 90:
                p = p + deltaAngle
            pantilthat.pan(p) 
            time.sleep(0.005)
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left  ')
            if (p - deltaAngle) > -90:    
                p = p - deltaAngle
            pantilthat.pan(p)
            time.sleep(0.005)
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down  ')
            if (t + deltaAngle) < 90:
                t = t + deltaAngle
            pantilthat.tilt(t)
            time.sleep(0.005)
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up    ')
            if (t - deltaAngle) > -90:
                t = t - deltaAngle
            pantilthat.tilt(t)
            time.sleep(0.005)            
finally:
    # Shut down cleanly
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    pantilthat.pan(0)
    pantilthat.tilt(0)
    time.sleep(1)            
