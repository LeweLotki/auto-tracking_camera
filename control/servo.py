import RPi.GPIO as GPIO
import pigpio
from time import sleep

# S3305

class servo:

    def __init__(self, pin : int):

        self.pin = pin
        self.pwm = pigpio.pi()
        self.current_angle = 0
        self.current_frequency = 50
        self.min_pulse_width = 500
        self.max_pulse_width = 2500
        self.min_angle = 0
        self.max_angle = 180
        # 6 * time to rotate 60d * delay
        self.delay_coef = 1.4
        self.cycle_time = 6 * 0.23 * self.delay_coef  

        self.__setup()
        self.__calibrate()

    def __del__(self): GPIO.cleanup()
    
    def __calibrate(self):

        angle = 0
        pulse_width = self.__get_pulse_width(angle)
        self.pwm.set_servo_pulsewidth(self.pin, pulse_width)
        
        sleep(3)

        self.current_angle = angle
        print('CALIBRATED')

    def __setup(self):

        self.pwm.set_mode(self.pin, pigpio.OUTPUT)
        self.pwm.set_PWM_frequency(self.pin, self.current_frequency)

    def __get_pulse_width(self, angle : float):

        pulse_width = (angle / self.max_angle)*(self.max_pulse_width - self.min_pulse_width) + self.min_pulse_width
        return pulse_width

    def __get_motion_time(self, angle : float):

        angle_diff = angle - self.current_angle if angle > self.current_angle else self.current_angle - angle
        print("angle_diff: ",angle_diff)
        motion_time = (angle_diff / 360) * self.cycle_time
        return motion_time

    def cleanup(self):

        self.pwm.set_PWM_dutycycle(self.pin, 0)
        self.pwm.set_PWM_frequency(self.pin, 0)

    def set_angle(self, angle : float):

        pulse_width = self.__get_pulse_width(angle)
        motion_time = self.__get_motion_time(angle)
        self.pwm.set_servo_pulsewidth(self.pin, pulse_width)
        print('motion time: ',motion_time)
        print('pulse_width: ',pulse_width)
        sleep(motion_time)

        self.current_angle = angle
        print(angle)

    def change_angle(self, angle_increment : float):

        angle = self.current_angle + angle_increment
        if angle > 180: angle = 180
        elif angle < 0: angle = 0

        self.set_angle(angle)

if __name__ == '__main__':

    servo_13 = servo(pin=13)

    try:

        for i in range(5):

            servo_13.change_angle(180)
            servo_13.change_angle(-90)
            servo_13.change_angle(-90)

    finally: servo_13.cleanup()
