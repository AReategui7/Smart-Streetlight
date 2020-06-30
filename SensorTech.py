# These are the libraries that have been imported.
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

# Camera is flipped to playback in the correct angle. - Alberto R.
camera.vflip = True
# This function is designed to make sure that the sound sensor will trigger video recording. - Alberto R. and Shalom D.
def Sound_tick(mic):
    if GPIO.input(mic) is GPIO.HIGH:
        camera.start_recording('Slap.h264')
        time.sleep(10)
        camera.start_recording()
        pir.wait_for_no_motion()

# These lines of code ensure that the sound sensor is activated when a snap or loud noise occurs, running the function. - Alberto R.
GPIO.add_event_detect(mic, GPIO.BOTH, bouncetime = 500)
GPIO.add_event_callback(mic, Sound_tick)

# When the motion sensor is tripped, the camera will preview, and start recording when the sound is sensed. - Shalom D.
while True:
    pir.wait_for_motion()
    print("Motion Detected!")
    time.sleep(3)
