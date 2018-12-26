#Importing Libraries
import time
from gpiozero import DistanceSensor, Buzzer, CamJamKitRobot


pinTrigger = 17 #17th GPIO Pin
pinEcho = 18 #18th GPIO pin
pinBuzzer = 21 #21st GPIO pin

robot = CamJamKitRobot() #Robot initialisation
buzzer = Buzzer(pinBuzzer) #Buzzer initialisation
sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger) #Sensor initialisation - feed the GPIO pins

robot.forward() #Move the robot forward
time.sleep(1) #Move it for 1 second
robot.stop() #After 1 second, stop the robot
try:
    while True: 
        value = sensor.distance * 100 #Get the value
        if value < 20: #In there's an object 20cm or less infront of the sensor (car)
            buzzer.on() #Set off the buzzer and make your cat go crazy!
		else: #If there is not object is range
	    	buzzer.off() #Make sure the buzzer is off
        	print("Distance: %.1f cm" % value) #Print the value for debugging
        	time.sleep(1) #Wait a second before re-iterating

except KeyboardInterrupt: #CRTL-C to exit
    print("Exiting") #Exit message
