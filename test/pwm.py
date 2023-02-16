# RPi.GPIOのライブラリを「GPIO」という名前で使います
import RPi.GPIO as GPIO
import time

# GPIOのピン番号指定を「BCM」に設定します
GPIO.setmode(GPIO.BCM)

# PWMに使うピンを「Out」に設定します
GPIO.setup(17,GPIO.OUT)

# PWMに使うピンと周波数(1秒間に50回)を設定します
pwm = GPIO.PWM(17,50)

# PWMの制御を開始します
pwm.start(0)

for num in range(100):
    pwm.ChangeDutyCycle(num)
    print(num)
    time.sleep(0.1)
    

print("done.")
pwm.stop()

# GPIOの設定を解除します
GPIO.cleanup(17)