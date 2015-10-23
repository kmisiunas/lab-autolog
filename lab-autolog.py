# python code
# 
# by kmisiunas 

from sense_hat import SenseHat
import time
import urllib2
import os 


### PARAMETERS ###

updateInterval = 30 # in sec = 5min

serverURL = "http://data.sparkfun.com/input/"

publicKey = "OGzNYR7mdEFgYOON7g8m"

privateKey = "8beDvBJZ91fezaag4eNl"

accelerometerUpdateInterval = 0.1 # in sec


### CODE ###

sense = SenseHat()

def sendInforToServer( sense, vibration ):
   "reads infor and sends it to the server"
   url = serverURL + publicKey + "?private_key=" + privateKey
   url += "&temp=%.3f" % sense.get_temperature()
   url += "&humidity=%.3f" % sense.get_humidity()
   url += "&pressure=%.1f" % sense.get_pressure()
   url += "&cpu_temp=%.3f" % cpuTemp()
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
   
def cpuTemp():
   tmp = float( os.popen('cat /sys/class/thermal/thermal_zone0/temp').readline() )
   return (tmp/1000)
   


# Init

## Clear the screen
#sense.show_message("")
sense.clear(0, 0, 0)
sense.low_light = True

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
  #if(time.time() >= timeOldAccelerometer):
   # vibrationDetector(sense, vibration)
    #timeOldAccelerometer += accelerometerUpdateInterval
    #if( time.time() - timeOldAccelerometer > 10*  accelerometerUpdateInterval):
      #print( 'Falling behind accelerometers schedule at ' + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) )
  # blink LED somewhere
  green = (0, 255, 0)
  blue = (0, 0, 255)
  if( int(time.time()) == 0 ):
    sense.set_pixel(0, 0, green)
  else:
    sense.set_pixel(0, 0, blue)
  # CPU rest
  #time.sleep(0.05)


# Log failure
print( 'lab-autolog shutdown at ' + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) )

# print red X on the hat to let the user know that t needs restatting
X = [255, 0, 0]  # Red
O = [0, 0, 0]  # White

question_mark = [
X, O, O, O, O, O, O, X,
O, X, O, O, O, O, X, O,
O, O, X, O, O, X, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, X, O, O, O,
O, O, X, O, O, X, O, O,
O, X, O, O, O, O, X, O,
X, O, O, O, O, O, O, X
]

sense.set_pixels(question_mark)
