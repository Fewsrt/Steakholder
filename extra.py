import socket
import time
import BlynkLib
from gpiozero import CPUTemperature

#cmsensor1
#BLYNK_AUTH = 'nD-SwPo3-WpMrvAbdksIFa4YnP14l9-A'

#cmsensor2
BLYNK_AUTH = 'S2nsQqctQF1oAwCumBtBJrKQZ7FdgjU4'
blynk = BlynkLib.Blynk(BLYNK_AUTH,server='blynk.honey.co.th',port=8080)

while True:
    blynk.run()
    testIP = "8.8.8.8"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((testIP, 0))
    ipaddr = s.getsockname()[0]
    host = socket.gethostname()
    cpu = CPUTemperature()
    blynk.virtual_write(19, str(ipaddr))
    blynk.virtual_write(20, str(host))
    blynk.virtual_write(21, "Temp CPU : " + str(cpu.temperature) + "  C")
    blynk.virtual_write(22, cpu.temperature)
    print(cpu.temperature)
    print ("IP:", ipaddr, " Host:", host)
    time.sleep(5)

