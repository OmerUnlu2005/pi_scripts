import wiringpi
import time


#SETUP
print("Start")
pinLed = 2
pinSwitch = 1
wiringpi.wiringPiSetup()
wiringpi.pinMode(pinLed, 1)
wiringpi.pinMode(pinSwitch, 0)

# infinity loop
while True:
    if(wiringpi.digitalRead(pinSwitch) == 0):
        print("Button pressed")
        time.sleep(0.05)
        wiringpi.digitalWrite(pinLed, 1)
    else:
        print("Button released")
        time.sleep(0.5)
        wiringpi.digitalWrite(pinLed, 0)