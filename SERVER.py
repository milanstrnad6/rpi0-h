#BOOT MODULE:SERVER

import subprocess
import time

import DATAMANAGER

#ACTIONS

def boot():
    duration = DATA.loadWaitForInternetConnection()
    time.sleep(duration)
    subprocess.call(['/home/pi/Desktop/rpi0-h/serverStart.sh'])

#MAIN

boot()
