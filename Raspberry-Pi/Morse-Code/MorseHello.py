import RPi.GPIO as GPIO
import time

# Create 'Hello World' in Morse Code
# Dot = 1 unit
# Dash = 3 units
# Space between parts of the same letter = 1 unit
# Space betewwen letters = 3 units
# Space between words = 7 units
# 1 unit = .2 seconds
# 'Hello World' in Morse: **** * *-** *-** ---   *-- --- *-* *--* -**

#creating the 'dot' blink
def dot():
    GPIO.output(11, True)
    time.sleep(.2)
    GPIO.output(11,False)
    time.sleep(.2)

# creating the 'dash' blink
def dash():
    GPIO.output(11, True)
    time.sleep(.6)
    GPIO.output(11,False)
    time.sleep(.2)

# letter space
def letter():
    GPIO.output(11,False)
    time.sleep(.6)

# word space
def space():
    GPIO.output(11,False)
    time.sleep(1.4)

# dots, dashes, and spaces to blink out "Hello World" in morse code
while True:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    dot()
    dot()
    dot()
    dot()
    letter()
    dot()
    letter()
    dot()
    dash()
    dot()
    dot()
    letter()
    dot()
    dash()
    dot()
    dot()
    letter()
    dash()
    dash()
    dash()
    space()
    dot()
    dash()
    dash()
    letter()
    dash()
    dash()
    dash()
    letter()
    dot()
    dash()
    dot()
    letter()
    dot()
    dash()
    dot()
    dot()
    letter()
    dash()
    dot()
    dot()
    space()
    GPIO.cleanup()
    
