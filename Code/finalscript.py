#Import Libraries
import xbox
import time 
from gpiozero import DistanceSensor, Buzzer, CamJamKitRobot

joy = xbox.Joystick() #Initialise joystick (xbox 360 controller)
robot = CamJamKitRobot() #Initialise Robot

def moveBackwards(value):
    if value < 0.1: #If the value is less than 0.1
	   return #Do nothing, because at 0.1 the wheels don't even have enough power to turn - no point doing anything.
    robot.backward(value) #If the value is more than 0.1, move the robot back with the desired power

def moveForwards(value):
    if value < 0.1: #If the value is less than 0.1
       return #Do nothing, because at 0.1 the wheels don't even have enough power to turn - no point doing anything.
    robot.forward(value) #If the value is more than 0.1, move the robot forward with the desired power

def turn(value):
    if value < 0: #If the value is negative (or the stick is to the left)
        value = value * -1 #Make the value positive
    	if value < 0.1: #If the value is less than 0.1
	       return #Do nothing, because at 0.1 the wheels don't even have enough power to turn - no point doing anything.
	robot.left(value) #If the value is more than 0.1, turn the robot left with the desired power
    else: #If the value is NOT negative (or the stick is to the right)
	   if value < 0.1: #If the value is less than 0.1
	       return #Do nothing, because at 0.1 the wheels don't even have enough power to turn - no point doing anything.
	   robot.right(value) #If the value is more than 0.1, turn the robot right with the desired power



try:
    while True: #Loop
        robot.stop() #Stop the robot (initialise)
        if joy.rightTrigger() != 0: #If a value from the right trigger is retreived 
		    moveForwards(joy.rightTrigger()) #Move forwards with the value retreived
        if joy.leftTrigger() != 0: #If a value from the left trigger is retreived 
		    moveBackwards(joy.leftTrigger()) #Move backwards with the value retreived
        if joy.leftStick()[0] != 0: #[0] = x value (tuple is returned - (x,y))
 		    turn(joy.leftStick()[0]) #Turn with value
        
        time.sleep(0.2) #Wait a little before re-iteration

except KeyboardInterrupt: # CTRL-C Exit
    print("Exiting") #Exit message





robot.stop()

