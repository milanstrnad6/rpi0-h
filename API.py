#API

from flask import request
from flask_api import FlaskAPI

import DATA
# import APNS

#PROPERTIES

app = FlaskAPI(__name__)

#ENDPOINTS

@app.route('/deviceInit/', methods=["GET"])
def deviceInit():
    print("API - DEVICE INIT")
    if request.method == "GET":
        time = HISTORY.save_deviceInit()

    return {"data":{"time":time}}

@app.route('/getData/')
def getData():
    print("API - getData")
    if request.method == "GET":
        temperatures = DATAMANAGER.loadTemperatures()
        humidities = DATAMANAGER.loadHumidities()

    return {"data":{"temperatures": ""}}

#MAIN

if __name__ == "__main__":
    app.run()
