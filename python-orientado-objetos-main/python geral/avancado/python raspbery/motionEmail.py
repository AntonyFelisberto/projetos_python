import RPi.GPIO as GPIO
import requests
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.IN)
url="https://maker.ifttt.com/trigger/motion_detected/json/with/key/mkK5u4TfiAeqVhv7-LeXBA9fdrBW7-C6JcI4DansRye"
while(True):
	x=GPIO.input(21)
	if(x==1):
		print("sending email")
		r=requests.get(url)
		print("response: ",r.text)
	else:
		print("No motion detected")
