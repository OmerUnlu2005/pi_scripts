import wiringpi
import time
import sys

def on(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(1)

def off(_pin):
    wiringpi.digitalWrite(_pin, 0)
    time.sleep(1)

def long(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(1.5)
    wiringpi.digitalWrite(_pin, 0)


def short(_pin):
    wiringpi.digitalWrite(_pin, 1)
    time.sleep(0.5)
    wiringpi.digitalWrite(_pin, 0)


#SETUP
print("Start")
pin1 = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1, 1)

pin2 = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin2, 1)

pin3 = 3
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin3, 1)

#MAIN
for l in range(0,10):
    short(pin1)
    long(pin2)
    short(pin3)

#cleanup
print("Done")