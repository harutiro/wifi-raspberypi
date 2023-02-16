import time

#GPIOの初期設定
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

#GPIO18を入力端子設定
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.OUT)


try:
    while True:
        #スイッチ状態取得
        sw_status = GPIO.input(18)

        #画面出力
        if sw_status == 0:
            print('スイッチON!')
            GPIO.output(17, 1)
        else:
            print('')
            GPIO.output(17, 0)

        #少し待つ
        time.sleep(0.3)    

except KeyboardInterrupt:
  # GPIO設定クリア
  GPIO.cleanup()