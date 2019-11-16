#BOOT MODULE:SERVER

import subprocess
import time

import DATAMANAGER

#ACTIONS

def boot():
    duration = DATAMANAGER.loadWaitForInternetConnection()
    time.sleep(duration)
    subprocess.call(['/home/pi/Desktop/FINAL/rpi0-h/serverStart.sh'])

#MAIN

boot()
