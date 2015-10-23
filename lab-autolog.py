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

def sendInforToServer( sense, vibration ):
   "function_docstring"
   function_suite
   return [expression]
   
def vibrationDetector( sense, vibration ):
   "function_docstring"
   function_suite
   return [expression]   


# Init

## Clear the screen


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
    timeOld += acceleroterUpdateInterval
    if( time.time() - timeOldAccelerometer > 10*  accelerometerUpdateInterval):
      print( 'Falling behind accelerometers schedule at ' + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) )
  
  # blink LED somewhere
  


# Log failure
print( 'lab-autolog shutdown at ' + time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()) )

# print red X on the hat to let the user know that t needs restatting
