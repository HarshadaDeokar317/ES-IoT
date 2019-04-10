import subprocess

import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

i=0


    while True:
            input_state = GPIO.input(12)
            if input_state == 0:
                    subprocess.call("fswebcam -d /dev/video0 -r 1024x768 -S0 "+str(i)+"pic.jpg",shell=True)
                    print('PIC CAPTURED')
                    i=i+1
                    time.sleep(0.2)

        GPIO.cleanup()