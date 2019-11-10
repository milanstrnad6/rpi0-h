#MANAGER:DATA

import FILES

#PROPERTIES

FILENAME_TH = '/home/pi/Desktop/rpi0-h/DATA/th.txt'
ROW_WAIT_FOR_INTERNET_CONNECTION = 3

FILENAME_TEMPERATURES = '/home/pi/Desktop/rpi0-h/DATA/temperatures.txt'
FILENAME_HUMIDITIES = '/home/pi/Desktop/rpi0-h/DATA/humidities.txt'

#ACTIONS:TH

def loadWaitForInternetConnection():
    return int(FILES.loadline(FILENAME_TH,ROW_WAIT_FOR_INTERNET_CONNECTION))

def loadTemperatures():
	return FILES.load(FILENAME_TEMPERATURES)

def loadHumidities():
	return FILES.load(FILENAME_HUMIDITIES)
