import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import requests

import pyowm




app = Flask(__name__)


@app.route("/")
def hello():
    
    owm = pyowm.OWM('e9acf144f807e0e7bd7795178be89775')
    observation = owm.weather_at_place('Grand Rapids,us')
    w = observation.get_weather()
    t = w.get_temperature('celsius')
    t = t['temp']
    t = (t*1.800) + 32
    print t

    w = str(w)
    w = w.split('=')
    w =  w[2][:-1]    
    w = "Status: " + w + " - Temperature: " + str(t)   
    

    return w



@app.route('/getweather')
def getweather():



    return "hello"
    

@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
