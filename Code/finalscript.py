#Import Libraries
import xbox
import time 
from gpiozero import Buzzer, CamJamKitRobot

class Robot:
    def __init__(self, joystick, buzzer):
	self.robot = CamJamKitRobot()  #Initialise Robot
	self.buzzer = buzzer
	self.joy = joystick

    def listen(self):
	"""Method to start listening for controller presses"""
	try:
            while True:
		self.buzzer.off()
	        self.robot.stop()  
                while self.joy.rightTrigger() != 0: #On right trigger press
                    if self.joy.rightTrigger() < 0.15:
                        continue
                    self.robot.forward(joy.rightTrigger())
                while self.joy.leftTrigger() != 0: #On left trigger press
                    if self.joy.leftTrigger() < 0.15:
                        continue
                    self.robot.backward(joy.leftTrigger())
                while self.joy.leftStick()[0] != 0: #On left stick move
		    if self.joy.leftStick()[0] < 0:
			value = self.joy.leftStick()[0] * -1
			if value < 0.15:
            		    continue
			self.robot.left(value)
		    else:
			if (self.joy.leftStick()[0] < 0.15):
			    continue
                        self.robot.right(self.joy.leftStick()[0])
		    while self.joy.A():
		    	self.buzzer.on()
                    time.sleep(0.2) #Wait between iterations
                if self.joy.B():
                    self.robot.stop()
        except KeyboardInterrupt: #CTRL-C
            print("Exiting")
        finally:
            self.robot.stop() #Stop robot
            self.joy.close() #Cleanup

buzzer = Buzzer(17)
joy = xbox.Joystick() #Initialise joystick (xbox 360 controller)
robot = Robot(joy, buzzer) #Instantiate robot class with joystick
robot.listen() #Start listening

