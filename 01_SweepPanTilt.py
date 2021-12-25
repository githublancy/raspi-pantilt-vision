#!/usr/bin/env python
# Continuously sweep the pan and tilt mechanism
# Ctrl-C to quit
import math
import time
import pantilthat

while True:
    # Get the current time in seconds
    t = time.time()
 
    # Generate an angle using a sine wave (-1 to 1) multiplied by 90 (-90 to 90)
    # Keeping at 85 since my servos seem to struggle between 87 and 90
    a = math.sin(t * 2) * 85
   
    # Cast a to an int
    a = int(a)
    
    # These functions take a number between 90 and -90 and set the
    # pan servo and tilt servo to that number of degrees 
    pantilthat.pan(a)
    pantilthat.tilt(a)
    print(a)
 
    # Sleep to give the HAT a rest
    time.sleep(0.005)
