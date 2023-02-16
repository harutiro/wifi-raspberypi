import time

#GPIOの初期設定
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#GPIO18を入力端子設定
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

pwm = GPIO.PWM(22,50)




try:
    GPIO.output(22, 1)
    GPIO.output(13, 1)
    pwm.start(0)


    while True:
        pwm.ChangeDutyCycle(100)

        str = input()
        if str == "w" :
          GPIO.output(17, 0)
          GPIO.output(27, 1)
          GPIO.output(5, 1)
          GPIO.output(6, 0)
        elif str == "s":
          GPIO.output(17, 1)
          GPIO.output(27, 0)
          GPIO.output(5, 1)
          GPIO.output(6, 0)



        
        # GPIO.output(5, 0)
        # GPIO.output(6, 1)
        #少し待つ
        # time.sleep(3)   




        # GPIO.output(17, 1)
        # GPIO.output(27, 1)
        # GPIO.output(5, 1)
        # GPIO.output(6, 1)
        # #少し待つ
        # time.sleep(3)  

        # pwm.ChangeDutyCycle(100)
        # GPIO.output(17, 1)
        # GPIO.output(27, 0)
        # GPIO.output(5, 1)
        # GPIO.output(6, 0)
        # #少し待つ
        # time.sleep(3)  


        # GPIO.output(17, 0)
        # GPIO.output(27, 0)
        # GPIO.output(5, 0)
        # GPIO.output(6, 0)
        # #少し待つ
        # time.sleep(3)   

       

except KeyboardInterrupt:
  # GPIO設定クリア
  GPIO.cleanup()

  print("done.")
  pwm.stop()  
