#GPIOの初期設定
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
while True:
    GPIO.output(16,1)
    print(1)

    time.sleep(1)

    GPIO.output(16,0)
    print(0)

    time.sleep(1)

