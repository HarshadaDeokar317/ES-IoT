import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(36, GPIO.OUT)

while(True):
	if GPIO.input(8)==1:
		GPIO.output(36, GPIO.LOW)
		print 'ir detected'
		time.sleep(0.2)
	else:
		GPIO.output(36, GPIO.HIGH)
		print 'ir not detected'
