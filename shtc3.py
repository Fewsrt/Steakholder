# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
#
# SPDX-License-Identifier: MIT
import BlynkLib
import time
import busio
import board
import adafruit_shtc3

# time.sleep(40)

BLYNK_AUTH = 'S2nsQqctQF1oAwCumBtBJrKQZ7FdgjU4'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH, server='blynk.honey.co.th', port=8080)

i2c = busio.I2C(board.SCL, board.SDA)
sht = adafruit_shtc3.SHTC3(i2c)

temperature, relative_humidity = sht.measurements


@blynk.on("connected")
def blynk_connected():
    print("Updating V1,V2,V3 values from the server...")
    blynk.sync_virtual(40, 41)
    print("status OK")


# @blynk.on("readV40")
# def v40_read_handler():
#     blynk.virtual_write(40, temperature)


# @blynk.on("readV41")
# def v41_read_handler():
#     blynk.virtual_write(41, relative_humidity)


while True:
    blynk.run()
    blynk.virtual_write(40, temperature)
    blynk.virtual_write(41, relative_humidity)
    print("Temperature: %0.2f" % temperature)
    print("Humidity: %0.2f" % relative_humidity)
    print("")
    time.sleep(2)
