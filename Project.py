import time
import wiringpi
import paho.mqtt.client as mqtt
from bmp280 import BMP280
from smbus2 import SMBus, i2c_msg

# Create an I2C bus object
bus = SMBus(0)
address1 = 0x23 # i2c address
address2 = 0x76

# MQTT settings
MQTT_HOST ="mqtt3.thingspeak.com"
MQTT_PORT = 1883
MQTT_KEEPALIVE_INTERVAL = 60
MQTT_TOPIC = "channels/2462234/publish"
MQTT_CLIENT_ID = "Cg45ARIZBzQvNRcJOSwNHSg"
MQTT_USER = "Cg45ARIZBzQvNRcJOSwNHSg"
MQTT_PWD = "wLKoY/+JcfiKiShbnKt/cj09"


# Setup BH1750 and BMP280 and LED
bus.write_byte(address1, 0x10)
bytes_read = bytearray(2)

bmp280 = BMP280(i2c_addr= address2, i2c_dev=bus)
interval = 15 # Sample period in seconds

pin1 = 2
wiringpi.wiringPiSetup()
wiringpi.pinMode(pin1, 1)

def get_value(bus, address):
    write = i2c_msg.write(address, [0x10]) # 1lx resolution 120ms see datasheet
    read = i2c_msg.read(address, 2)
    bus.i2c_rdwr(write, read)
    bytes_read = list(read)
    return (((bytes_read[0]&3)<<8) + bytes_read[1])/1.2 # conversion see datasheet

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("Connected OK with result code "+str(rc))
    else:
        print("Bad connection with result code "+str(rc))

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected result code "+str(rc))

def on_message(client,userdata,msg):
    print("Received a message on topic: " + msg.topic + "; message: " + msg.payload)


# Set up a MQTT Client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, MQTT_CLIENT_ID)
client.username_pw_set(MQTT_USER, MQTT_PWD)

# Connect callback handlers to client
client.on_connect= on_connect
client.on_disconnect= on_disconnect
client.on_message= on_message

print("Attempting to connect to %s" % MQTT_HOST)
client.connect(MQTT_HOST, MQTT_PORT)
client.loop_start() #start the loop

while True:
    lux = get_value(bus, address1)
    bmp280_temperature = bmp280.get_temperature()
    bmp280_pressure = bmp280.get_pressure()
    bh1750_light = lux.get_light_intensity()
    print("{:.2f} Lux".format(lux))
    print("Temperature: %4.1f, Pressure: %4.1f" % (bmp280_temperature, bmp280_pressure))
    if lux < 50:
        wiringpi.digitalWrite(pin1, 1)
    else:
        wiringpi.digitalWrite(pin1, 0)
    time.sleep(interval)
    # Create the JSON data structure
    MQTT_DATA = "field1="+str(bmp280_temperature)+"&field2="+str(bmp280_pressure)+"&field3="+str(bh1750_light)+"&status=MQTTPUBLISH"
    print(MQTT_DATA)
    try:
        client.publish(topic=MQTT_TOPIC, payload=MQTT_DATA, qos=0, retain=False, properties=None)
        time.sleep(interval)
    except OSError:
        client.reconnect()