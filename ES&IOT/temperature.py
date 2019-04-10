



import RPi.GPIO as GPIO
from smbus import SMBus
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
led=[15, 16, 18, 19, 21, 22, 23, 24]
for i in range(8):
	GPIO.setup(led[i], GPIO.OUT)
bus = SMBus(1)
bus.write_byte(0x48, 0)
last_reading=-1
p=GPIO.PWM(7,100)
p.start(0)
while(0==0):
	reading = bus.read_byte(0x48)
	if(reading != last_reading):
		write=(255/1023)*reading
		print('output:'+str(reading))
	last_reading=reading
#	p.ChangeDutyCycle(0)
	if(reading < 27):
			p.ChangeDutyCycle(0)
			GPIO.output(led[0], GPIO.HIGH)
			time.sleep(0.05)

	if(reading > 30):
			p.ChangeDutyCycle(20)
			GPIO.output(led[1], GPIO.HIGH)
			GPIO.output(led[0], GPIO.HIGH)
			time.sleep(0.05)

	if(reading > 35):
			p.ChangeDutyCycle(30)
			GPIO.output(led[2], GPIO.HIGH)
			time.sleep(0.05)

	if(reading > 40):
			p.ChangeDutyCycle(40)
			GPIO.output(led[3], GPIO.HIGH)
			time.sleep(0.05)

	if(reading > 45):
			p.ChangeDutyCycle(50)
			GPIO.output(led[4], GPIO.HIGH)
			time.sleep(0.05)

	if(reading > 50):
			p.ChangeDutyCycle(65)
			GPIO.output(led[5], GPIO.HIGH)
			time.sleep(0.05)

	if(reading > 65):
			p.ChangeDutyCycle(85)
			GPIO.output(led[6], GPIO.HIGH)
			GPIO.output(led[7], GPIO.HIGH)
                	time.sleep(0.05)
        else:
                        GPIO.output(led[6], GPIO.LOW)
                        GPIO.output(led[7], GPIO.LOW)
                        GPIO.output(led[0], GPIO.LOW)
                        GPIO.output(led[1], GPIO.LOW)
                        GPIO.output(led[2], GPIO.LOW)
                        GPIO.output(led[3], GPIO.LOW)
                        GPIO.output(led[4], GPIO.LOW)
                        GPIO.output(led[5], GPIO.LOW)
                        time.sleep(0.05)

