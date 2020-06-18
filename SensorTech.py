import numpy as np
from gpiozero import LED
from gpiozero import MotionSensor
import GPIO
import camera
import time

# This is the LED that will turn on. - Shalom D.
red_led = LED(18)

# This sets the motion sensor up. From here we will control its actions. - Alberto R.
pir = MotionSensor(4)

# This sets up the camera that we will use to record any action. - Alberto R.
camera = camera.camera()

# These lines set the mic channel and sound sensor up. - Alberto R.
mic = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(mic, GPIO.IN)

# Motion Sensor will wait for any motion to be detected. - Alberto R.
pir.wait_for_motion()

# When the motion sensor is tripped, the camera will preview, and start recording when the sound is sensed. - Shalom D.
while True:
    pir.wait_for_motion()
    print("Motion Detected!")
    camera.start_preview()
    if GPIO.input(mic) is HIGH:
        camera.start_recording('Slap.h264')
        time.sleep(10)
        camera.stop_recording()
    pir.wait_for_no_motion()
    camera.stop_preview()

# When the motion sensor is tripped, the previewing will begin, then record for 10 secs, then stop previewing. - Alberto R.
while True:
    pir.wait_for_motion()
    print("Motion Detected!")
    camera.start_preview()
    camera.start_recording('NewSense.h264')
    time.sleep(15)
    camera.stop_recording()
    camera.stop_preview()
    # can you see this
    # yes, I can
