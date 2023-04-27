import RPi.GPIO as GPIO
from time import sleep

class led:

    def __init__(self, pin : int):

        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)

    def __del__(self):

        GPIO.output(self.pin, GPIO.LOW)

    def set_brightness(self, state : int):
        
        if state == 0:

            GPIO.output(self.pin, GPIO.LOW)

        else:

            GPIO.output(self.pin, GPIO.HIGH)


if __name__ == '__main__':

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    led_green = led(pin=8)
    led_green.set_brightness(state=1)

    sleep(5)
