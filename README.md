# raspi-pantilt-vision
Control the Pan-Tilt HAT on a Raspberry Pi and provide basic vision capabilities using a mounted camera

## Pre-Requisites
Set up your Raspberry Pi and update/upgrade to the latest Raspberry Pi OS: https://www.raspberrypi.com/software/

## Code Samples

### 01_SweepPanTilt.py
Continuously sweep the pan-tilt mechanism in a sinusoidal action. <br>
Use ctrl-q to quit.

### 02_SetPanTilt.py
Set the pan-tilt mechanism to fixed positions.

### 03_KeyboardPanTilt.py
Control the pan and tilt mechanism in 5 degrees angle increments using keyboard arrow keys. <br>
Use q to quit.

### 04_WebPanTilt.py
Control the pan and tilt mechanism using a web page with arrow buttons. <br>
After running this script, point the browser to http://0.0.0.0:9595/ <br>
Use ctrl-c to quit.

### 05_KeyboardPanTilt_Camera.py
Control the pan and tilt mechanism in 5 degrees angle increments using keyboard arrow keys while viewing the camera feed in a window. <br>
Use p to take a still picture. <br>
Use q to quit.

## References
Pimoroni Pan-Tilt HAT: https://shop.pimoroni.com/products/pan-tilt-hat <br>
Pimoroni Pan-Tilt HAT Software and Examples: https://github.com/pimoroni/pantilt-hat <br>
Core Electronics Tutorial: https://core-electronics.com.au/tutorials/pan-tilt-hat-raspberry-pi.html <br>
