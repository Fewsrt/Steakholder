#pip3 install blynk-library-python
#sudo pip3 install adafruit-circuitpython-shtc3

#from __future__ import print_function
import BlynkLib
import time
#import busio
#import board
#import adafruit_shtc3
import RPi.GPIO as GPIO

time.sleep(40)

BLYNK_AUTH = 'S2nsQqctQF1oAwCumBtBJrKQZ7FdgjU4'

blynk = BlynkLib.Blynk(BLYNK_AUTH,server='blynk.honey.co.th', port=8080)

#i2c = busio.I2C(board.SCL, board.SDA)
#sht = adafruit_shtc3.SHTC3(i2c)

relay1 = 37
relay2 = 35
relay3 = 33
relay4 = 31
relay5 = 29
relay6 = 15
relay7 = 13
relay8 = 11
#statustimer = '0'

x3 = ''
x4 = ''


GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(relay1,GPIO.OUT)
GPIO.setup(relay2,GPIO.OUT)
GPIO.setup(relay3,GPIO.OUT)
GPIO.setup(relay4,GPIO.OUT)
GPIO.setup(relay5,GPIO.OUT)
GPIO.setup(relay6,GPIO.OUT)
GPIO.setup(relay7,GPIO.OUT)
GPIO.setup(relay8,GPIO.OUT)

@blynk.on("connected")
def blynk_connected():
    print("Updating values from the server...")
    blynk.sync_virtual(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)
    print("status OK")

#@blynk.on("V22")
#def v22_write_handler(value):
#    #print('Current slider value: {}'.format(value[0]))
#    statustimer = format(value[0])
#    print(type(statustimer))
#    print(statustimer)
    #timer = x22

@blynk.on("V1")
def v1_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x1 = format(value[0])
    if x1 == "1":
        GPIO.output(relay1,GPIO.HIGH)
        print("relay1-work")
    else:
        GPIO.output(relay1,GPIO.LOW)
        print("relay1-not-work")

@blynk.on("V2")
def v2_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x2 = format(value[0])
    if x2 == "1":
        GPIO.output(relay2,GPIO.HIGH)
        print("relay2-work")
    else:
        GPIO.output(relay2,GPIO.LOW)
        print("relay2-not-work")

@blynk.on("V3")
def v3_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x3 = format(value[0])
    if x3 == "1":
        GPIO.output(relay3,GPIO.HIGH)
        GPIO.output(relay1,GPIO.HIGH)
        print("relay3-work")
        print("relay1-work")
    else:
        GPIO.output(relay3,GPIO.LOW)
        if x4 == 1:
            GPIO.output(relay1,GPIO.HIGH)
            print("relay1-work")
        else:
            GPIO.output(relay1,GPIO.LOW)
            print("relay1-not-work")
        print("relay3-not-work")

@blynk.on("V4")
def v4_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x4 = format(value[0])
    if x4 == "1":
        GPIO.output(relay4,GPIO.HIGH)
        GPIO.output(relay1,GPIO.HIGH)
        print("relay4-work")
    else:
        GPIO.output(relay4,GPIO.LOW)
        if x3 == 1:
            GPIO.output(relay1,GPIO.HIGH)
            print("relay1-work")
        else:
            GPIO.output(relay1,GPIO.LOW)
            print("relay1-not-work")
        print("relay4-not-work")

@blynk.on("V5")
def v5_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x5 = format(value[0])
    if x5 == "1":
        GPIO.output(relay5,GPIO.HIGH)
        print("relay5-work")
    else:
        GPIO.output(relay5,GPIO.LOW)
        print("relay5-not-work")

@blynk.on("V6")
def v6_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x6 = format(value[0])
    if x6 == "1":
        GPIO.output(relay6,GPIO.HIGH)
        print("relay6-work")
    else:
        GPIO.output(relay6,GPIO.LOW)
        print("relay6-not-work")

@blynk.on("V7")
def v7_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x7 = format(value[0])
    if x7 == "1":
        GPIO.output(relay7,GPIO.HIGH)
        print("relay7-work")
    else:
        GPIO.output(relay7,GPIO.LOW)
        print("relay7-not-work")

@blynk.on("V8")
def v8_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x8 = format(value[0])
    if x8 == "1":
        GPIO.output(relay8,GPIO.HIGH)
        print("relay8-work")
    else:
        GPIO.output(relay8,GPIO.LOW)
        print("relay8-not-work")

@blynk.on("V9")
def v9_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x9 = format(value[0])
    if x9 == "1":
        GPIO.output(relay1,GPIO.HIGH)
        blynk.virtual_write(1, 1)
        print("relay1-work")
    else:
        GPIO.output(relay1,GPIO.LOW)
        blynk.virtual_write(1, 0)
        print("relay1-not-work")

@blynk.on("V10")
def v10_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x10 = format(value[0])
    if x10 == "1":
        GPIO.output(relay2,GPIO.HIGH)
        blynk.virtual_write(2, 1)
        print("relay2-work")
    else:
        GPIO.output(relay2,GPIO.LOW)
        blynk.virtual_write(2, 0)
        print("relay2-not-work")

@blynk.on("V11")
def v11_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x11 = format(value[0])
    if x11 == "1":
        GPIO.output(relay3,GPIO.HIGH)
        blynk.virtual_write(3, 1)
        print("relay3-work")
    else:
        GPIO.output(relay3,GPIO.LOW)
        blynk.virtual_write(3, 0)
        print("relay3-not-work")

@blynk.on("V12")
def v12_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x12 = format(value[0])
    if x12 == "1":
        GPIO.output(relay4,GPIO.HIGH)
        blynk.virtual_write(4, 1)
        print("relay4-work")
    else:
        GPIO.output(relay4,GPIO.LOW)
        blynk.virtual_write(4, 0)
        print("relay4-not-work")

@blynk.on("V13")
def v13_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x13 = format(value[0])
    if x13 == "1":
        GPIO.output(relay5,GPIO.HIGH)
        blynk.virtual_write(5, 1)
        print("relay5-work")
    else:
        GPIO.output(relay5,GPIO.LOW)
        blynk.virtual_write(5, 0)
        print("relay5-not-work")

@blynk.on("V14")
def v14_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x14 = format(value[0])
    if x14 == "1":
        GPIO.output(relay6,GPIO.HIGH)
        blynk.virtual_write(6, 1)
        print("relay6-work")
    else:
        GPIO.output(relay6,GPIO.LOW)
        blynk.virtual_write(6, 0)
        print("relay6-not-work")

@blynk.on("V15")
def v15_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x15 = format(value[0])
    if x15 == "1":
        GPIO.output(relay7,GPIO.HIGH)
        blynk.virtual_write(7, 1)
        print("relay7-work")
    else:
        GPIO.output(relay7,GPIO.LOW)
        blynk.virtual_write(7, 0)
        print("relay7-not-work")

@blynk.on("V16")
def v16_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x16 = format(value[0])
    if x16 == "1":
        #print("timer-on")
        #if statustimer == '1':
            GPIO.output(relay8, GPIO.HIGH)
            blynk.virtual_write(8, 1)
            print("relay8-work")
    else:
        GPIO.output(relay8, GPIO.LOW)
        blynk.virtual_write(8, 0)
        print("relay8-not-work")
              


#@blynk.on("readV17")
#def v17_read_handler():
#    temperature, relative_humidity = sht.measurements
#    blynk.virtual_write(17, temperature)

#@blynk.on("readV18")
#def v18_read_handler():
#    temperature, relative_humidity = sht.measurements
#    blynk.virtual_write(18, relative_humidity)


while True:
    blynk.run()
