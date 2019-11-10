#API

from flask import request
from flask_api import FlaskAPI

import DATAMANAGER

#PROPERTIES

app = FlaskAPI(__name__)

#ENDPOINTS

@app.route('/getData/')
def getData():
    print("API - getData")
    if request.method == "GET":
        temperatures = DATAMANAGER.loadTemperatures()
        humidities = DATAMANAGER.loadHumidities()

    return {"data":{
        "temperatures": temperatures, 
        "humidities": humidities
    }}

#MAIN

if __name__ == "__main__":
    app.run()
