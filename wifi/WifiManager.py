from MotorSetting import Motor
from CompassSetting import Compass
from GpsSetting import Gps
import RPi.GPIO as GPIO
import time
import math

motor = Motor()
compass = Compass()
gps = Gps()