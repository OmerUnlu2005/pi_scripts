import time
import wiringpi
from smbus2 import SMBus, i2c_msg

# Create an I2C bus object
bus = SMBus(0)
address = 0x23 # i2c address

# Setup BH1750
bus.write_byte(address, 0x10)
bytes_read = bytearray(2)

pin1 = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1, 1)

def get_value(bus, address):
    write = i2c_msg.write(address, [0x10]) # 1lx resolution 120ms see datasheet
    read = i2c_msg.read(address, 2)
    bus.i2c_rdwr(write, read)
    bytes_read = list(read)
    return (((bytes_read[0]&3)<<8) + bytes_read[1])/1.2 # conversion see datasheet

while True:
    lux = get_value(bus, address)
    print("{:.2f} Lux".format(lux))
    if lux < 50:
        wiringpi.digitalWrite(pin1, 1)
    else:
        wiringpi.digitalWrite(pin1, 0)
    time.sleep(1)
