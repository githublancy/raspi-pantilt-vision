#!/usr/bin/env python
# Set the pan and tilt mechanism to fixed points
import time
import pantilthat
from array import *

# Disable servos on timeout. Setiing to 1/2 second to allow range of motion to complete
pantilthat.idle_timeout(0.5)

# Sleep time
s = 2

# Fixed Points
# Setting extremes to 85 rather than 90 to protect pantilt mechanism
panArray = array('i',  [-85, -45,  0, 45, 85])
tiltArray = array('i', [-85, -45,  0, 45, 85])

for p in panArray:
    for t in tiltArray:
        print('Pan:', p, ' Tilt:', t)
        pantilthat.pan(p)
        pantilthat.tilt(t)
        time.sleep(s)

print('Pan: 0, Tilt: 0')
pantilthat.pan(0)
pantilthat.tilt(0)
time.sleep(s)
