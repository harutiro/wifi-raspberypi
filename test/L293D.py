import time

#GPIOの初期設定
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#GPIO18を入力端子設定
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)




try:
    GPIO.output(22, 1)
    GPIO.output(13, 1)


    while True:
        # GPIO.output(17, 0)
        # GPIO.output(27, 1)
        # #少し待つ
        # time.sleep(3)   

        # GPIO.output(17, 1)
        # GPIO.output(27, 1)
        # #少し待つ
        # time.sleep(3)  

        # GPIO.output(17, 1)
        # GPIO.output(27, 0)
        # #少し待つ
        # time.sleep(3)  

        # GPIO.output(17, 0)
        # GPIO.output(27, 0)
        # #少し待つ
        # time.sleep(3)   


        GPIO.output(5, 0)
        GPIO.output(16, 1)
        print("6") 
        #少し待つ
        time.sleep(3)
          

        GPIO.output(5, 1)
        GPIO.output(16, 1)
        print("5,6")  
        #少し待つ
        time.sleep(3) 
         

        GPIO.output(5, 1)
        GPIO.output(16, 0)
        print("5")  
        #少し待つ
        time.sleep(3) 
         

        GPIO.output(5, 0)
        GPIO.output(16, 0)
        print("なし")
        #少し待つ
        time.sleep(3) 
        

except KeyboardInterrupt:
  # GPIO設定クリア
  GPIO.cleanup()