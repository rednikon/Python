import RPi.GPIO as GPIO
import time

# Write a Raspberry Pi program that makes an LED on your breadboard blink on and off.
while True:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,True)
    time.sleep(2)
    GPIO.output(11,False)
    time.sleep(2)
    GPIO.cleanup()
    
