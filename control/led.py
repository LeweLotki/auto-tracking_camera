import RPi.GPIO as GPIO
from time import sleep

class led:

    def __init__(self, pin : int):

        self.pin = 32 
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)

        self.pwm_led = GPIO.PWM(self.pin, 100)
        self.pwm_led.start(0)

    def __del__(self):

        GPIO.output(self.pin, GPIO.LOW)

    def set_brightness(self, duty_cycle : int):
        
        if duty_cycle == 0:

            GPIO.output(self.pin, GPIO.HIGH)
            self.pwm_led.ChangeDutyCycle(duty_cycle)
            GPIO.output(self.pin, GPIO.LOW)

        else:

            GPIO.output(self.pin, GPIO.HIGH)
            self.pwm_led.ChangeDutyCycle(duty_cycle)


if __name__ == '__main__':

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    led_green = led(pin=32)
    led_green.set_brightness(duty_cycle=100)

    sleep(5)
