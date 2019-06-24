#Import all the libraries
import RPi.GPIO as GPIO
import time
from pubnub import Pubnub
 
# Initialize the Pubnub Keys 
pub_key = "pub-c-8f8e7b3a-e8af-4336-8a99-d8b927f29969"
sub_key = "sub-c-43cff576-92a3-11e9-9769-e24cdeae5ee1"
 
LIGHT = 18           #define pin of RPi on which you want to take output
 
def init():          #initalize the pubnub keys and start subscribing
 
 global pubnub    #Pubnub Initialization
 GPIO.setmode(GPIO.BCM)
 GPIO.setwarnings(False)
 GPIO.setup(LIGHT,GPIO.OUT)
 GPIO.output(LIGHT, False) 
 pubnub = Pubnub(publish_key=pub_key,subscribe_key=sub_key)
 pubnub.subscribe(channels='alexaTrigger', callback=callback, error=callback, reconnect=reconnect, disconnect=disconnect)
 
 
def control_alexa(controlCommand):          #this function control Aalexa, commands received and action performed
 if(controlCommand.has_key("trigger")):
  if(controlCommand["trigger"] == "light" and controlCommand["status"] == 1):
   GPIO.output(LIGHT, True) 
   print "light is on"
  else:
   GPIO.output(LIGHT, False) 
   print "light is off"
 else:
  pass
 
 
 
def callback(message, channel):        #this function waits for the message from the aleatrigger channel
 if(message.has_key("requester")):
  control_alexa(message)
 else:
  pass
 
 
def error(message):                    #if there is error in the channel,print the  error
 print("ERROR : " + str(message))
 
 
def reconnect(message):                #responds if server connects with pubnub
 print("RECONNECTED")
 
 
def disconnect(message):               #responds if server disconnects with pubnub
 print("DISCONNECTED")
 
 
if __name__ == '__main__':
 init()                    #Initialize the Script
 

