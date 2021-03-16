# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
import BlynkLib
import time
import busio
import board
import adafruit_shtc3

BLYNK_AUTH = 'S2nsQqctQF1oAwCumBtBJrKQZ7FdgjU4'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH,server='blynk.honey.co.th',port=8080)

i2c = busio.I2C(board.SCL, board.SDA)
sht = adafruit_shtc3.SHTC3(i2c)

@blynk.on("connected")
def blynk_connected():
    print("Updating V1,V2,V3 values from the server...")
    blynk.sync_virtual(17,18)
    print("status OK")

@blynk.on("readV17")
def v17_read_handler():
    temperature, relative_humidity = sht.measurements
    blynk.virtual_write(17,sht.temperature)

@blynk.on("readV18")
def v18_read_handler():
    temperature, relative_humidity = sht.measurements
    blynk.virtual_write(18,sht.relative_humidity)

while True:
    blynk.run()
    temperature, relative_humidity = sht.measurements
    print("Temperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % relative_humidity)
    print("")
    time.sleep(5)

