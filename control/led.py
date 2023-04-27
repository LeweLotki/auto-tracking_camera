import RPi.GPIO as GPIO
from time import sleep

class led:

    def __init__(self, led_pin : int):

        self.led_pin = 32 
        GPIO.setup(led_pin, GPIO.OUT, initial=GPIO.LOW)

        self.pwm_led = GPIO.PWM(led_pin, 100)
        self.pwm_led.start(0)

    def __del__(self):

        GPIO.output(self.led_pin, GPIO.LOW)

    def set_brightness(self, duty_cycle : int):

        GPIO.output(self.led_pin, GPIO.HIGH)
        self.pwm_led.ChangeDutyCycle(duty_cycle)

if __name__ == '__main__':

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    led_green = led(led_pin=32)
    led_green.set_brightness(duty_cycle=100)

    sleep(5)
