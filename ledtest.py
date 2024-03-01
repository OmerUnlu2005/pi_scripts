import wiringpi
import time
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(0.1)
    wiringpi.digitalWrite(_pin, 0)
    time.sleep(0.1)


#SETUP
print("Start")
pin1 = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1, 1)


#MAIN
for i in range(0,10):
    blink(pin1)
#cleanup
print("Done")