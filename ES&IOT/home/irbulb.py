import RPi.GPIO as GPIO 
from time import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(11, GPIO.OUT)

def binary_aquire(pin, duration):
    t0 = time()
    results = []
    while (time() - t0) < duration:
        results.append(GPIO.input(pin))
    return results


def on_ir_receive(pinNo, bouncetime=150):
    data = binary_aquire(pinNo, bouncetime/1000.0)
    if len(data) < bouncetime:
        return
    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    
    for i in range(1, len(data)):
        if (data[i] != data[i-1]) or (i == len(data)-1):
            pulses.append((data[i-1], int((i-i_break)/rate*1e6)))
            i_break = i
    outbin = ""
    for val, us in pulses:
        if val != 1:
            continue
        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 < us < 2000:
            outbin += "1"
    try:
        return int(outbin, 2)
    except ValueError:
        return None


def destroy():
    GPIO.cleanup()


if __name__ == "__main__":
    setup()
    p=GPIO.PWM(11, 100)
    p.start(100)
    try:
        print(".........Starting IR Receiver............")
	print("PRESS mode=BULB ON, VOL-=BULB ON 20%, VOL+=BULB ON 80%, EQ=BULB OFF ")
        while True:
            GPIO.wait_for_edge(31, GPIO.FALLING)
            code = on_ir_receive(31)
            if code:
		if code==33446055:
			p.ChangeDutyCycle(30)
			print "mode"
			print "Bulb Brightness=30%"
			time()
		
		if code==33464415:
                	p.ChangeDutyCycle(50)
                        print "VOL-"
                        print "Bulb Brightness=20%"
			time()
		
	        if code==33448095:
                	p.ChangeDutyCycle(10)
                        print "VOL+"
                        print "Bulb Brightness=80%"
			time()
		
		if code==33431775:
                	p.ChangeDutyCycle(100)
                        print "EQ"
                        print "Bulb OFF"

    except KeyboardInterrupt:
        pass
    except RuntimeError:
        pass
    destroy()
