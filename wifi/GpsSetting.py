import serial
import time
import string
import pynmea2
import math

class Gps:

    pole_radius = 6356752.314245                  # 極半径
    equator_radius = 6378137.0                    # 赤道半径


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
    
    def cal_distance(self,nowLocation ,nextLocation):

        # 緯度経度をラジアンに変換
        nowLat = math.radians(nowLocation[0])
        nowLon = math.radians(nowLocation[1])
        nexLat = math.radians(nextLocation[0])
        nexLon = math.radians(nextLocation[1])

        lat_difference = nowLat - nexLat       # 緯度差
        lon_difference = nowLon - nexLon       # 経度差
        lat_average = (nowLat + nexLat) / 2    # 平均緯度

        e2 = (math.pow(self.equator_radius, 2) - math.pow(self.pole_radius, 2)) \
                / math.pow(self.equator_radius, 2)  # 第一離心率^2

        w = math.sqrt(1- e2 * math.pow(math.sin(lat_average), 2))

        m = self.equator_radius * (1 - e2) / math.pow(w, 3) # 子午線曲率半径

        n = self.equator_radius / w                         # 卯酉線曲半径

        distance = math.sqrt(math.pow(m * lat_difference, 2) \
                    + math.pow(n * lon_difference * math.cos(lat_average), 2)) # 距離計測

        # print(distance / 1000)

        return distance / 1000
        
        
            