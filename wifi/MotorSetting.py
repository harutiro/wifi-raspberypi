import time

#GPIOの初期設定
import RPi.GPIO as GPIO

class Motor:

    left = 1
    right = 2
    non = 0
    # pwm = GPIO.PWM(22,50)

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        # 左右よう
        GPIO.setup(17, GPIO.OUT)
        GPIO.setup(27, GPIO.OUT)
        GPIO.setup(22, GPIO.OUT)

        # 前後よう
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(13, GPIO.OUT)
        

    def back(self , direction , sleepTime):

        print(direction)

        # 向き
        GPIO.output(22, 1)
        if direction == self.left :
            GPIO.output(17, 1)
            GPIO.output(27, 0)
        elif direction == self.right :
            GPIO.output(17, 0)
            GPIO.output(27, 1)
        else :
            GPIO.output(17, 1)
            GPIO.output(27, 1)
        
        # 移動
        GPIO.output(13, 1)
        GPIO.output(5, 0)
        GPIO.output(16, 1)

        time.sleep(sleepTime)

        #　リセット
        self.clean()
        return
    
    def forward(self , direction , sleepTime):
        print(direction)

        # 向き
        GPIO.output(22, 1)
        if direction == self.left :
            GPIO.output(17, 1)
            GPIO.output(27, 0)
        elif direction == self.right :
            GPIO.output(17, 0)
            GPIO.output(27, 1)
        else :
            GPIO.output(17, 1)
            GPIO.output(27, 1)
        
        # 移動
        GPIO.output(13, 1)
        GPIO.output(5, 1)
        GPIO.output(16, 0)

        time.sleep(sleepTime)

        #　リセット
        self.clean()
        return
    
    def clean(self):
        GPIO.output(13, 0)
        GPIO.output(5, 0)
        GPIO.output(16, 0)

        GPIO.output(17, 0)
        GPIO.output(27, 0)
        GPIO.output(22, 0)

