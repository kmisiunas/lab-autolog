# python code
# 
# by kmisiunas 

from sense_hat import SenseHat
import sched, time
import urllib2, httplib
import os, random, colorsys, math, json


### PARAMETERS ###

intervalSendToServer = 5*60 # in sec = 5min
intervalMeasurment = 10 # sec
intervalAccelerometer = 0.1 # sec


serverURL = "http://data.sparkfun.com/input/"

# read kays from a file
with open('keys.json') as keys_file: 
   keys = json.load(keys_file)
publicKey = str(keys["public"])
privateKey = str(keys["private"])

# MathWorks ThingSpeak
thingSpeakServer = "https://api.thingspeak.com"
thingSpeakKey = str(keys["thingSpeakKey"])

# temp calibration
tempOffset = -2.3
tempScale = 1.0


### CODE ###

def sendDataToServer():
   "reads infor and sends it to the server"
   schedule.enter( intervalSendToServer, 1, sendDataToServer, () ) # reoccuring 
   print("debug: send data request at "+ time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) )
   url = serverURL + publicKey + "?private_key=" + privateKey
   vals = "&temp=%.2f" % (sum(temp)/len(temp))
   vals += "&humidity=%.3f" % (sum(humidity)/len(humidity))
   vals += "&pressure=%.3f" % (sum(pressure)/len(pressure))
   vals += "&cpu_temp=%.2f" % cpuTemp()
   vals += "&light=%.3f" % 0.0
   vals += "&vibration=%.3f" % 0.0
   vals += "&vibration_peaks=%.3f" % 0.0
   #send data via GET
   try:
      f = urllib2.urlopen(url + vals, timeout = 1)
      #s = f.read()
      f.close()
   except Exception as e:
     print("There was an error: %r" % e) 
   #Send ToThingSpeak via POST
   params = urllib.urlencode({
      'temp': (sum(temp)/len(temp)), 
      'humidity': (sum(humidity)/len(humidity)), 
      'pressure': (sum(pressure)/len(pressure)),
      'cpu_temp': cpuTemp(),
      'light': 0.0,
      'vibration' : 0.0,
      'vibration_peaks' : 0.0,
      'key': thingSpeakKey })
   headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
   conn = httplib.HTTPConnection("api.thingspeak.com:80")
   conn.request("POST", "/update", params, headers)
   #response = conn.getresponse() # dont need?
   clearAccumulate()
   
def tempCalibrated():
   return (sense.get_temperature() + tempOffset) * tempScale
   
def cpuTemp():
   tmp = float( os.popen('cat /sys/class/thermal/thermal_zone0/temp').readline() )
   return (tmp/1000)
   
def measureAccumulate():
   "Function for accumulating measurements"
   schedule.enter( intervalMeasurment, 2, measureAccumulate, () ) # reoccuring 
   global temp, humidity, pressure
   temp.append( tempCalibrated() )
   humidity.append( sense.get_humidity() )
   pressure.append( sense.get_pressure() )
   print("temp " + str(tempCalibrated()))
   
def clearAccumulate():
   "Function for clearing accumulated data forn new averaging"
   global temp, humidity, pressure
   temp = []
   pressure = []
   humidity = []
   
def readAndResetVibration( vibration ):
   "sends infor to the server"
   return []   
   
def vibrationDetector( sense, vibration ):
   "function_docstring"
   return []   

def playGame():
   "play game with LED to let user know that the device is active"
   temp = max(-1.0, min( 1.0, (tempCalibrated() -21)/2  )) # range 19-21-23 in -1  to 1
   speed = 0.8 - temp*0.5
   schedule.enter( speed , 3, playGame, () ) # reooccuring 
   global gX, gY, gPos
   if(random.random() > 0.7 - temp*0.2): gameNewDirection()
   sense.set_pixel(gPos[0], gPos[1], (0,0,0) ) #old pixel off
   gPos[0] = gPos[0] + gX
   gPos[1] = gPos[1] + gY
   gameBounce()
   color = colorsys.hsv_to_rgb((1-temp)*0.5 * 0.66  , 1.0, 1.0)
   sense.set_pixel(gPos[0], gPos[1], (int(color[0]*255), int(color[1]*255), int(color[2]*255)) ) # new pixel off
      
def gameBounce():
   "plater bounces from the walls" 
   global gX, gY, gPos
   maxLine = 8
   if( gPos[0] < 0 ):
      gPos[0] = 0
      gX = 1
   if( gPos[0] >= maxLine ):
      gPos[0] = maxLine-1
      gX = -1
   if( gPos[1] < 0 ):
      gPos[1] = 0
      gY = 1
   if( gPos[1] >= maxLine ):
      gPos[1] = maxLine-1
      gY = -1
   
def gameNewDirection():
   global gX, gY
   gX = round( random.random() * 2 - 1)
   gY = round( random.random() * 2 - 1)
   if( gX == 0 and gY == 0 ): 
      gameNewDirection()

###  Init ###

schedule = sched.scheduler(time.time, time.sleep) # time events!

sense = SenseHat()

## Clear the screen
#sense.show_message("")
sense.clear(0, 0, 0)
sense.low_light = True

# Prepare arrays 
clearAccumulate()
gPos = [4,4]
gX = 0
gY = 0

# Start
schedule.enter( 0, 1, measureAccumulate, () )  
schedule.enter( 60 - (int(time.time()) % 60) , 1, sendDataToServer, () )  
schedule.enter( 5 , 3, playGame, () )  

schedule.run()


# Shotdown?
# print( 'lab-autolog shutdown at ' + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) )
