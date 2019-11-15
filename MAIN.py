#BOOT MODULE:CUBE

import RPi.GPIO as IO
import time

import DATAMANAGER
import SENSOR

#PROPERTIES

BOOTING_EXTRATIME = 5 #seconds
WAIT_FOR_NEXT_CHECK = 10 #120 #seconds

#ACTIONS

def boot():
    print("*** BOOT ***")
    IO.setmode(IO.BCM)
    IO.setwarnings(0)

    ULTRASOUND.setup()
    PUMP.setup()
    LED.setup()

    duration = DATA.loadWaitForInternetConnection() + BOOTING_EXTRATIME
    #LED.bootBlinking(duration)

    start()

#UTILITIES

def start():
    obj = HTU21D()

    print("*[TH - START]*")
    while True:
	print("*[TH - CHECK]*")

       	#temperature = obj.read_tmperature()
        print "Temp:", obj.read_tmperature(), "C"
    	time.sleep(WAIT_FOR_NEXT_CHECK)

#MAIN

boot()
