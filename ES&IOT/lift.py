import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(35,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(36,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(38,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)

GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

num=0
var1=0
var2=0
var3=0
var4=0
var5=0
var6=var7=var8=var9=var10=0
p=1

def led(m,ch):
	if((m>=0) & (m<=3)):
		if ch == 0:
			GPIO.output(23,GPIO.LOW)
			GPIO.output(24,GPIO.HIGH)
		elif ch == 1:
			GPIO.output(23,GPIO.LOW)
			GPIO.output(24,GPIO.LOW)
			GPIO.output(22,GPIO.LOW)
			GPIO.output(21,GPIO.HIGH)
		elif ch == 2:
			GPIO.output(22,GPIO.LOW)
			GPIO.output(21,GPIO.LOW)
			GPIO.output(19,GPIO.LOW)
			GPIO.output(18,GPIO.HIGH)
		elif ch == 3:
			GPIO.output(18,GPIO.LOW)
			GPIO.output(19,GPIO.LOW)
			GPIO.output(16,GPIO.LOW)
			GPIO.output(15,GPIO.HIGH)
	elif m>3:
		if ch == 3:
			GPIO.output(15,GPIO.LOW)
			GPIO.output(16,GPIO.HIGH)
		elif ch == 2:
			GPIO.output(15,GPIO.LOW)
			GPIO.output(16,GPIO.LOW)
			GPIO.output(18,GPIO.LOW)
			GPIO.output(19,GPIO.HIGH)
		elif ch == 1:
			GPIO.output(18,GPIO.LOW)
			GPIO.output(19,GPIO.LOW)
			GPIO.output(21,GPIO.LOW)
			GPIO.output(22,GPIO.HIGH)
		elif ch == 0:
			GPIO.output(22,GPIO.LOW)
			GPIO.output(21,GPIO.LOW)
			GPIO.output(23,GPIO.HIGH)
			GPIO.output(24,GPIO.HIGH)
			
		
while True:
	if (GPIO.input(38)==0 and var1==0 ):#0
			GPIO.output(3,GPIO.LOW)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(8,GPIO.LOW)
			GPIO.output(10,GPIO.LOW)
			GPIO.output(11,GPIO.LOW)
			GPIO.output(12,GPIO.HIGH)
			GPIO.output(13,GPIO.HIGH)
			if var6==1:
				led(4,0)
			else:
				led(0,0)
			time.sleep(1)
			var2=var6=0
			var1=1
			var4=var5=var3=p=1
			var7=var8=var9=1
	elif (GPIO.input(37)==0 and var6==0):#1
			GPIO.output(3,GPIO.HIGH)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(8,GPIO.HIGH)
			GPIO.output(10,GPIO.HIGH)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.HIGH)
			GPIO.output(13,GPIO.HIGH)
			if (var3==1 and p==0):
				led(4,1)
			else:
				led(0,1)
			time.sleep(1)
			num=0
			var1=var3=var7=p=0
			var6=var5=1
	elif (GPIO.input(36)==0 and var3==0):#2
			GPIO.output(3,GPIO.LOW)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.HIGH)
			GPIO.output(8,GPIO.LOW)
			GPIO.output(10,GPIO.LOW)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.LOW)
			GPIO.output(13,GPIO.HIGH)
			if (var5 == 1 and p==1):
				led(4,2)
			else:
				led(0,2)
			time.sleep(1)
			var6=var5=var4=p=0
			var3=var1=1
	elif (GPIO.input(35)==0 and var5==0):#3
			GPIO.output(3,GPIO.LOW)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(8,GPIO.LOW)
			GPIO.output(10,GPIO.HIGH)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.LOW)
			GPIO.output(13,GPIO.HIGH)
			led(0,3)
			time.sleep(1)
			var1=var6=var5=var4=p=1
			var3=var9=var8=0
	elif (GPIO.input(37)==0 and var8==0):#3-1
			GPIO.output(3,GPIO.LOW)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.HIGH)
			GPIO.output(8,GPIO.LOW)
			GPIO.output(10,GPIO.LOW)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.LOW)
			GPIO.output(13,GPIO.HIGH)
			led(4,2)
			time.sleep(1)
			GPIO.output(3,GPIO.HIGH)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(8,GPIO.HIGH)
			GPIO.output(10,GPIO.HIGH)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.HIGH)
			GPIO.output(13,GPIO.HIGH)
			led(4,1)
			time.sleep(1)
			var1=var3=var7=0
			var8=var5=1
	elif (GPIO.input(35)==0 and var7==0):#1-3
			GPIO.output(3,GPIO.LOW)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.HIGH)
			GPIO.output(8,GPIO.LOW)
			GPIO.output(10,GPIO.LOW)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.LOW)
			GPIO.output(13,GPIO.HIGH)
			led(0,2)
			time.sleep(1)
			GPIO.output(3,GPIO.LOW)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(8,GPIO.LOW)
			GPIO.output(10,GPIO.HIGH)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.LOW)
			GPIO.output(13,GPIO.HIGH)
			led(0,3)
			time.sleep(1)
			var3=var8=var9=0
			var1=var5=var7=1
	elif (GPIO.input(38)==0 and var9==0):#3-0
			GPIO.output(3,GPIO.LOW)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.HIGH)
			GPIO.output(8,GPIO.LOW)
			GPIO.output(10,GPIO.LOW)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.LOW)
			GPIO.output(13,GPIO.HIGH)
			led(4,2)
			time.sleep(1)
			GPIO.output(3,GPIO.HIGH)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(8,GPIO.HIGH)
			GPIO.output(10,GPIO.HIGH)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.HIGH)
			GPIO.output(13,GPIO.HIGH)
			led(4,1)
			time.sleep(1)
			GPIO.output(3,GPIO.LOW)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(8,GPIO.LOW)
			GPIO.output(10,GPIO.LOW)
			GPIO.output(11,GPIO.LOW)
			GPIO.output(12,GPIO.HIGH)
			GPIO.output(13,GPIO.HIGH)
			led(4,0)		
			time.sleep(1)
			var1=var3=var5=var9=p=1
			var2=var6=0
	elif (GPIO.input(35)==0 and var2==0 ):#0-3
			GPIO.output(3,GPIO.HIGH)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(8,GPIO.HIGH)
			GPIO.output(10,GPIO.HIGH)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.HIGH)
			GPIO.output(13,GPIO.HIGH)
			led(0,1)
			time.sleep(1)
			GPIO.output(3,GPIO.LOW)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.HIGH)
			GPIO.output(8,GPIO.LOW)
			GPIO.output(10,GPIO.LOW)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.LOW)
			GPIO.output(13,GPIO.HIGH)
			led(0,2)
			time.sleep(1)
			GPIO.output(3,GPIO.LOW)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(8,GPIO.LOW)
			GPIO.output(10,GPIO.HIGH)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.LOW)
			GPIO.output(13,GPIO.HIGH)
			led(0,3)
			time.sleep(1)
			var1=var2=var4=var5=var6=1
			var3=var8=var9=0
	elif (GPIO.input(36)==0 and var2==0):#0-2
			GPIO.output(3,GPIO.HIGH)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(8,GPIO.HIGH)
			GPIO.output(10,GPIO.HIGH)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.HIGH)
			GPIO.output(13,GPIO.HIGH)
			led(0,1)
			time.sleep(1)
			GPIO.output(3,GPIO.LOW)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.HIGH)
			GPIO.output(8,GPIO.LOW)
			GPIO.output(10,GPIO.LOW)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.LOW)
			GPIO.output(13,GPIO.HIGH)
			led(0,2)
			time.sleep(1)
			var4=var5=var6=p=0
			var2=var1=var3=1
	elif (GPIO.input(38)==0 and var4==0):#2-0
			GPIO.output(3,GPIO.HIGH)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(8,GPIO.HIGH)
			GPIO.output(10,GPIO.HIGH)
			GPIO.output(11,GPIO.HIGH)
			GPIO.output(12,GPIO.HIGH)
			GPIO.output(13,GPIO.HIGH)
			led(4,1)
			time.sleep(1)
			GPIO.output(3,GPIO.LOW)
			GPIO.output(5,GPIO.LOW)
			GPIO.output(7,GPIO.LOW)
			GPIO.output(8,GPIO.LOW)
			GPIO.output(10,GPIO.LOW)
			GPIO.output(11,GPIO.LOW)
			GPIO.output(12,GPIO.HIGH)
			GPIO.output(13,GPIO.HIGH)
			led(4,0)
			time.sleep(1)
			var1=var3=var5=var7=p=1
			var8=var9=1
			var2=var6=0


