#Import Libraries
import xbox
import time 
from gpiozero import DistanceSensor, Buzzer, CamJamKitRobot

class Robot:
	def __init__(self, joystick):
		self.robot = CamJamKitRobot()  #Initialise Robot
		self.joy = joystick

	def listen(self):
		"""Method to start listening for controller presses"""
		try:
			while True:
				self.robot.stop() #Initialise Robot by stopping.
				if self.joy.rightTrigger() != 0: #On right trigger press
					self.moveForwards(joy.rightTrigger())
				if self.joy.leftTrigger() != 0: #On left trigger press
					self.moveBackwards(joy.leftTrigger())
				if self.joy.leftStick()[0] != 0: #On left stick move
					self.turn(self.joy.leftStick()[0])
				time.sleep(0.2) #Wait between iterations
		except KeyboardInterrupt: #CTRL-C
			print("Exiting")
		finally:
			self.robot.stop() #Stop robot
			self.joy.close() #Cleanup


	def moveBackwards(self, value):
		"""Method to move the robot backwards"""
		if value < 0.1: #If the value is less than 0.1 do nothing, because the wheels don't even have enough power to move.
			return
		self.robot.backward(value) #If value is more than 0.1, move with the desired power

	def moveForwards(self, value):
		"""Method to move the robot forwards"""
		if value < 0.1:
			return
		self.robot.forward(value)

	def turn(self, value):
		"""Method to turn the robot"""
		if value < 0:
			value = value * -1
			if value < 0.1:
				return
			self.robot.left(value)
		else:
			if value < 0.1:
				return
			self.robot.right(value)

joy = xbox.Joystick() #Initialise joystick (xbox 360 controller)
robot = Robot(joy) #Instantiate robot class with joystick
robot.listen() #Start listening
