import time
from gpiozero import DistanceSensor, Buzzer, CamJamKitRobot


pinTrigger = 17
pinEcho = 18
pinBuzzer = 21

robot = CamJamKitRobot()
buzzer = Buzzer(pinBuzzer)
sensor = DistanceSensor(echo=pinEcho, trigger=pinTrigger)

robot.forward()
time.sleep(1)
robot.stop()
try:
    while True:
        value = sensor.distance * 100
        if value < 20:
            buzzer.on()
	else:
	    buzzer.off()
        print("Distance: %.1f cm" % value)
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting")
