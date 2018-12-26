import xbox
import time 
from gpiozero import DistanceSensor, Buzzer, CamJamKitRobot

joy = xbox.Joystick()
robot = CamJamKitRobot()

def moveBackwards(value):
    if value < 0.1:
	return
    robot.backward(value)

def moveForwards(value):
    if value < 0.1:
	return
    robot.forward(value)

def turn(value):
    if value < 0:
        value = value * -1
    	if value < 0.1:
	    return
	robot.left(value)
    else:
	if value < 0.1:
	    return
	robot.right(value)



try:
    while True:
        robot.stop()
        if  joy.rightTrigger() != 0:
		moveForwards(joy.rightTrigger())
        if joy.leftTrigger() != 0:
		moveBackwards(joy.leftTrigger())
        if joy.leftStick()[0] != 0: #[0] = x value
 		turn(joy.leftStick()[0])
        
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Exiting")





robot.stop()

