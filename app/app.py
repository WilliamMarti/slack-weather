from flask import Flask

import os, requests, pyowm


app = Flask(__name__)

@app.route("/")
def index():

    owm = pyowm.OWM(os.environ['API_KEY']) 

    observation = owm.weather_at_place('Grand Rapids,us')
    w = observation.get_weather()
    t = w.get_temperature('celsius')
    t = t['temp']
    t = (t*1.800) + 32

    w = str(w)
    w = w.split('=')
    w =  w[2][:-1]    
    w = "Status: " + w + " - Temperature: " + str(t)   

    return w

if __name__ == "__main__":

    app.run(host='0.0.0.0')
