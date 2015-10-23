# python code
# 
# by kmisiunas 

from sense_hat import SenseHat
import time

### PARAMETERS ###

updateInterval = 5*60 # in sec = 5min

serverURL = "http://data.sparkfun.com/input/"

publicKey = "OGzNYR7mdEFgYOON7g8m"

privateKey = "8beDvBJZ91fezaag4eNl"

accelerometerUpdateInterval = 0.01 # in sec


### CODE ###

sense = SenseHat()
timeOld = time.time()
timeOldAccelerometer = time.time()

while(True):
  # check if time elapsed 
  if(time.time() >= timeOld):
    # Send infor to the server
    sendInforToServer()
    timeOld += updateInterval
    
  # Update aceleroter
  if(time.time() >= timeOldAccelerometer):
    vibrationDetector()
    timeOld += acceleroterUpdateInterval
    if( time.time() - timeOldAccelerometer > 10*  accelerometerUpdateInterval):
      print( 'Falling behind accelerometers schedule at ' + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) )
  


# Log failure!
