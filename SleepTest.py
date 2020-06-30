import numpy as np
from gpiozero import LED
from gpiozero import MotionSensor
import GPIO
import camera
import time
import datetime

# This is the LED that will turn on. - Shalom D.
red_led = LED(18)

# This sets the motion sensor up. From here we will control its actions. - Alberto R.
pir = MotionSensor(4)

# This sets up the camera that we will use to record any action. - Alberto R.
camera = camera.camera()
camera.vflip = True
# These lines set the mic & sensor channel and sound & motion sensor up. - Alberto R.
mic = 17
pin = 4 
GPIO.setmode(GPIO.BCM)
GPIO.setup(mic, GPIO.IN)
GPIO.setup(pin, GPIO.IN)

# This function will label the files individually by the date and time they were recorded.
def Save_file():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")

#The variable 'filename' will store the Save_file function
filename = Save_file()

# This function will be called when the motion sensor is activated. The camera will be activated
# when the motion sensor has detected the motion for five seconds, recording for five seconds. 
def Crime_Watch(pin):
        if GPIO.input(pin) is GPIO.HIGH:
            i = 0
            while i < 2:
                pir.wait_for_motion
                if pir.motion_detected:
                    print('Detecting...')
                i = i + 1
            print("There is too much activity going on. Motion unclear.")
            camera.start_recording(filename)
            time.sleep(5)
            camera.stop_recording()

# These lines of code will ensure that when the motion is detected,
# the function will be called and the conditions will be satisfied.
GPIO.add_event_detect(pin, GPIO.BOTH, bouncetime = 500)
GPIO.add_event_callback(pin, Crime_Watch)

# Infinite Loop that will wait for motion to be detected.
while True:
    pir.wait_for_motion()

