#!/usr/bin/slack-weather
import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

import requests

import pyowm

newname = "slack-weather"
from ctypes import cdll, byref, create_string_buffer
    
libc = cdll.LoadLibrary('libc.so.6')    #Loading a 3rd party library C
buff = create_string_buffer(len(newname)+1) #Note: One larger than the name (man prctl says that)
buff.value = newname                 #Null terminated string as it should be
libc.prctl(15, byref(buff), 0, 0, 0) #Refer to "#define" of "/usr/include/linux/prctl.h" for the misterious value 16 & arg[3..5] are zero as the man page says.


app = Flask(__name__)


@app.route("/")
def index():

    f = open('apikey.txt', 'r')
    apikey = f.readline().strip()
    owm = pyowm.OWM(apikey) 

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

if __name__ == "__main__":
    app.run(host='0.0.0.0')
