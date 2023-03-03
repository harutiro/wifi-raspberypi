import serial
import time
import string
import pynmea2

class Gps:

    def get_location(self):
        while True:
            port="/dev/ttyAMA0"
            ser=serial.Serial(port, baudrate=9600, timeout=0.5)
            dataout = pynmea2.NMEAStreamReader()
            newdata=ser.readline()

            if str(newdata).startswith("b'$GPGGA"):
                newmsg=pynmea2.parse(str(newdata)[2:-5].replace("*","0000*",1))
                lat=newmsg.latitude
                lon=newmsg.longitude
                
                return lat ,lon
        
        
            