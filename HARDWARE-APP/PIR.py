import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.IN) #PIR

try:
    time.sleep(2) #to stabilize sensor
    while True:
        if GPIO.input(23):
            print("Beep Boop")
            time.sleep(5)
        else:
            print("oof")
        time.sleep(5) #loop delay, should be less than detection delay
    
except:
    GPIO.cleanup()