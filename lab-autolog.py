# python code
# 
# by kmisiunas 

from sense_hat import SenseHat
import time
import urllib2

### PARAMETERS ###

updateInterval = 5*60 # in sec = 5min

serverURL = "http://data.sparkfun.com/input/"

publicKey = "OGzNYR7mdEFgYOON7g8m"

privateKey = "8beDvBJZ91fezaag4eNl"

accelerometerUpdateInterval = 0.05 # in sec


### CODE ###

sense = SenseHat()

def sendInforToServer( sense, vibration ):
   "reads infor and sends it to the server"
   url = serverURL + publicKey + "?private_key=" + privateKey
   url += "&temp=%.3f" % sense.get_temperature()
   url += "&humidity=%.3f" % sense.get_humidity()
   url += "&pressure=%.1f" % sense.get_pressure()
   url += "&cpu_temp=%.3f" % 0.0
   url += "&light=%.3f" % 0.0
   url += "&vibration=%.3f" % 0.0
   url += "&vibration_peaks=%.3f" % 0.0
   #send data via GET
   f = urllib2.urlopen(url)
   s = f.read()
   f.close()
   return []
   
def readAndResetVibration( vibration ):
   "sends infor to the server"
   return []   
   
def vibrationDetector( sense, vibration ):
   "function_docstring"
   return []   


# Init

## Clear the screen

# vibration: [ sum of |x|, sum of x^2, n] 
vibration = [0.0, 0.0, 0.0]
timeOld = time.time()
timeOldAccelerometer = time.time()

while(True):
  # check if time elapsed 
  if(time.time() >= timeOld):
    # Send infor to the server
    sendInforToServer(sense, vibration)
    timeOld += updateInterval
    
  # Update aceleroter
  if(time.time() >= timeOldAccelerometer):
    vibrationDetector(sense, vibration)
    timeOld += accelerometerUpdateInterval
    if( time.time() - timeOldAccelerometer > 10*  accelerometerUpdateInterval):
      print( 'Falling behind accelerometers schedule at ' + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) )
  
  # blink LED somewhere
  


# Log failure
print( 'lab-autolog shutdown at ' + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) )

# print red X on the hat to let the user know that t needs restatting
