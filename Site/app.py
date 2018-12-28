from flask import Flask, render_template, url_for, redirect
from gpiozero import CamJamKitRobot
import time

app = Flask(__name__)
robot = CamJamKitRobot()
@app.route("/")
def home():
	return render_template("home.html")

robot.stop()

if __name__ == '__main__':
	app.run(debug=True)
