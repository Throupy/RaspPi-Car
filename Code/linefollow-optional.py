#Import library
import time
from gpiozero import LineSensor

pinLineFollower = 25 #25st GPIO Pin

sensor = LineSensor(pinLineFollower) #Initialise sensor with GPIO pin number

def lineseen():
    print("Line seen")
    
def linenotseen():
    print("No line seen")
    
sensor.when_line = lineseen #If the sensor finds a line
sensor.when_no_line = linenotseen #If the sensor doens't find a line

try:
    while True:
        time.sleep(10) #Infinite loop
        
except KeyboardInterrupt:
    print("Exiting")