#MANAGER:DATA

import FILES
import TIMES

#PROPERTIES

FILENAME_TH = '/home/pi/Desktop/FINAL/rpi0-h/DATA/th.txt'
ROW_WAIT_FOR_INTERNET_CONNECTION = 3

FILENAME_TEMPERATURES = '/home/pi/Desktop/FINAL/rpi0-h/DATA/temperatures.txt'
FILENAME_HUMIDITIES = '/home/pi/Desktop/FINAL/rpi0-h/DATA/humidities.txt'

#ACTIONS:TH

def loadWaitForInternetConnection():
    return int(FILES.loadline(FILENAME_TH,ROW_WAIT_FOR_INTERNET_CONNECTION))

def loadTemperatures():
	return FILES.load(FILENAME_TEMPERATURES)

def loadHumidities():
	return FILES.load(FILENAME_HUMIDITIES)

def saveTemperature(temperature):
    data = FILES.load(FILENAME_TEMPERATURES)
    tempAsString = str(temperature)
    record = TIMES.stringFrom(TIMES.now())+"|"+tempAsString+"\n"
    data.append(record)
    FILES.save(FILENAME_TEMPERATURES,data)

def resetTemperatures():
    data = 'TEMPERATURES\n'
    FILES.save(FILENAME_TEMPERATURES,data)

resetTemperatures()