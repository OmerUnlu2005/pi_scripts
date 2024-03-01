import wiringpi
import time


#SETUP
print("Start")
LDRpin = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(LDRpin, 0)


while True:
    if(wiringpi.digitalRead(LDRpin) == 0):
        print("dark")
        time.sleep(0.1)
    else:
        print("light")
        time.sleep(0.1)