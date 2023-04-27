import RPi.GPIO as GPIO

def set_board():

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
