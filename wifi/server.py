from MotorSetting import Motor
from CompassSetting import Compass
from GpsSetting import Gps
from WifiManager import Manager
import RPi.GPIO as GPIO
import time

import math
 
manager = Manager()

manager.fitAngleToNextPoint(34.810857166666665 , 137.31436433333334)

# motor = Motor()
# compass = Compass()
# gps = Gps()

# motor.setup()
# motor.back(Motor.right,3)
# time.sleep(3)

# motor.forward(Motor.left,3)
# time.sleep(3)

# print(compass.get_bearing())
 
# location = gps.get_location()
# print(str(location[0]))
# print(str(location[1]))

# print(math.degrees(math.atan(-1)))



GPIO.cleanup()
