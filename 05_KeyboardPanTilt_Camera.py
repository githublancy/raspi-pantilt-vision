#!/usr/bin/env python
# Raspberry-Pi pan and tilt using arrow keys script
# 'q' will quit the application
# 'p' will take a picture
# Arrow keys will control the Pan Tilt Camera in 5 Degree angle increments
import curses
import os
import time
import picamera
import pantilthat

# Disable servos on timeout
pantilthat.idle_timeout(0.25)

# Set up the camera
camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview(fullscreen=False, window = (200,200,640,480))

# Flip the camera so the image is not upside down
camera.vflip = True
camera.hflip = True

# Initialize curses and get the screen window
screen = curses.initscr()

# Turn off input echoing
curses.noecho()

# Respond to keys immediately (don't wait for enter)
curses.cbreak()

# Map arrow keys to special values like KEY_RIGHT, KEY_UP etc.
screen.keypad(True)

# Set start up servo positions
p = 0
t = 0
pantilthat.pan(p)
pantilthat.tilt(t)

# Set up the picture name postfix for the first picture 
picNum = 1

# Set up arrow key angle change
deltaAngle = 5

# Main process to read keyboard and act
# Swap 'left' and 'right' processing to switch between SelfieView and FirstPersonView
try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            # If q is pressed quit
            pantilthat.pan(0)
            pantilthat.tilt(0)
            time.sleep(1)            
            break
        elif char == ord('p'):
            # If p is pressed take a photo
            camera.capture('image%s.jpg' % picNum)
            picNum = picNum + 1
            screen.addstr(0, 0, 'Picture taken! ')
        elif char == curses.KEY_RIGHT:
            screen.addstr(0, 0, 'right ')
            if (p + deltaAngle) < 90:
                p = p + deltaAngle
            pantilthat.pan(p) 
            time.sleep(0.005)
        elif char == curses.KEY_LEFT:
            screen.addstr(0, 0, 'left ')
            if (p - deltaAngle) > -90:    
                p = p - deltaAngle
            pantilthat.pan(p)
            time.sleep(0.005)
        elif char == curses.KEY_DOWN:
            screen.addstr(0, 0, 'down ')
            if (t + deltaAngle) < 90:
                t = t + deltaAngle
            pantilthat.tilt(t)
            time.sleep(0.005)
        elif char == curses.KEY_UP:
            screen.addstr(0, 0, 'up ')
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
    