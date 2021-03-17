import BlynkLib
import time
import busio
import board
import adafruit_shtc3

#time.sleep(40)

BLYNK_AUTH = 'f68tpybltbG5gc69dcqFVVuhTyPjn2SS'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH, server='blynk.honey.co.th', port=8080)

i2c = busio.I2C(board.SCL, board.SDA)
sht = adafruit_shtc3.SHTC3(i2c)

while True:
    blynk.run()
    temperature, relative_humidity = sht.measurements
    blynk.virtual_write(1, temperature)
    blynk.virtual_write(2, relative_humidity)
    print("Temperature: %0.1f C" % temperature)
    print("Humidity: %0.1f %%" % relative_humidity)
    print("")
    time.sleep(1)
