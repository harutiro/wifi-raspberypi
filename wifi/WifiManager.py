from MotorSetting import Motor
from CompassSetting import Compass
from GpsSetting import Gps
import RPi.GPIO as GPIO
import time
import math
from promise import Promise

class Manager():

    motor = Motor()
    compass = Compass()
    gps = Gps()

    def __init__(self):
        self.motor.setup()

    def calculateAngleToNextPoint(self,wifiLat,wifiLon,nextLat,nextLon):
        if wifiLat <= nextLat:
            ratio = (wifiLon - nextLon) / ( wifiLat - nextLat)
            deg = (math.degrees(math.atan(ratio)) - 90) * -1
            return deg
        else:
            ratio = (wifiLon - nextLon) / ( wifiLat - nextLat)
            deg = ((math.degrees(math.atan(ratio)) - 90) * -1 ) +180
            return deg
    
    # true 時計回り
    # false 反時計回り
    # current 現時点
    # target 採取的な角度
    def checkClockwise(self,current, target):
        if target>current :
            return not ( target  - current > 180)
        else :
            return current - target  > 180

    def getPromiseByFitAngleToNextPoint(self,nextLat,nextLon):
        def fitAngleToNextPoint(resolve, reject):
            wifiLocation = self.gps.get_location()
            nowAngle = self.compass.get_bearing()
            nextAngle = self.calculateAngleToNextPoint(
                wifiLocation[0],
                wifiLocation[1],
                nextLat,
                nextLon
            )

            
            # TODO:長時間動けなかった時に、助けを呼ぶシステムを書く
            if self.checkClockwise(nowAngle,nextAngle):
                self.rightRotation(nextAngle)
                resolve()
            else:
                self.leftRotation(nextAngle)
                resolve()
        
        return Promise(fitAngleToNextPoint)
    
    def rightRotation(self,nextAngle):        
        nowAngle = self.compass.get_bearing()
        while abs(nextAngle - nowAngle) > 30:
            self.motor.forward(self.motor.right,3)
            time.sleep(3)
            self.motor.back(self.motor.left,3)
            time.sleep(3)
            nowAngle = self.compass.get_bearing()
            print(f"今の向き : {nowAngle}  向きたい向き : {nextAngle}")
    
    def leftRotation(self,nextAngle):
        nowAngle = self.compass.get_bearing()
        while abs(nextAngle - nowAngle) > 30:
            self.motor.forward(self.motor.left,3)
            time.sleep(3)
            self.motor.back(self.motor.right,3)
            time.sleep(3)
            nowAngle = self.compass.get_bearing()
            print(f"今の向き : {nowAngle}  向きたい向き : {nextAngle}")

    def getPromiseByMoveToNextPoint(self,nextLat,nextLon):
        def moveToNextPoint(resolve, reject):
            nowLocation = self.gps.get_location()
            nowLat = nowLocation[0]
            nowLon = nowLocation[1]
            distance = self.gps.cal_distance((nowLat,nowLon),(nextLat,nextLon))

            # TODO:長時間動けなかった時に、助けを呼ぶシステムを書く
            while abs(distance) > 0.01:
                self.motor.forward(self.motor.non,5)

                nowLocation = self.gps.get_location()
                nowLat = nowLocation[0]
                nowLon = nowLocation[1]
                distance = self.gps.cal_distance((nowLat,nowLon),(nextLat,nextLon))
                print(f"今の場所{nowLat},{nowLon} 行きたい場所{nextLat},{nextLon} 距離{distance}")
            
            resolve()

        return Promise(moveToNextPoint)

