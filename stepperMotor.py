import wiringpi
import time
import sys

def blink(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(0.1)
    wiringpi.digitalWrite(_pin, 0)



#SETUP
print("Start")
pin1 = 3
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1, 1)

pin2 = 4
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin2, 1)

pin3 = 6
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin3, 1)

pin4 = 9
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin4, 1)


#MAIN
for i in range(0,400):
    blink(pin1)
    blink(pin2)
    blink(pin3)
    blink(pin4)
#cleanup
print("Done")