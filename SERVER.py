#BOOT MODULE:SERVER

import subprocess
import time

import DATA

#ACTIONS

def boot():
    duration = DATA.load_waitForInternetConnection()
    time.sleep(duration)
    subprocess.call(['/home/pi/Desktop/rpi0-h/serverStart.sh'])

#MAIN

boot()
