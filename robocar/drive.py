import Jetson.GPIO as GPIO
import time

from adafruit_blinka.microcontroller.tegra.t210.pin import Pin

from robocar.pins import (
    PWM_PIN_1,
    PWM_PIN_2,
    MOTOR1_DIRECTION_PIN_1,
    MOTOR1_DIRECTION_PIN_2,
    MOTOR2_DIRECTION_PIN_1,
    MOTOR2_DIRECTION_PIN_2,
)

turning_duration = 2


class DriveSystem:
    def __init__(self):
        self.pwm1, self.pwm2 = self._setup_pins()

    def _setup_pins(self):
        PWM_PIN_1.init(mode=Pin.OUT)
        PWM_PIN_2.init(mode=Pin.OUT)
        MOTOR1_DIRECTION_PIN_1.init(mode=Pin.OUT)
        MOTOR1_DIRECTION_PIN_2.init(mode=Pin.OUT)
        MOTOR2_DIRECTION_PIN_1.init(mode=Pin.OUT)
        MOTOR2_DIRECTION_PIN_2.init(mode=Pin.OUT)

        p1 = GPIO.PWM(PWM_PIN_1.id, 1000)
        p1.start(0)
        p2 = GPIO.PWM(PWM_PIN_2.id, 1000)
        p2.start(0)

        return p1, p2

    def forwards(self, speed=50):
        self._set_rhs_forward()
        self._set_lhs_forward()
        self.pwm1.start(speed)
        self.pwm2.start(speed)

    def backwards(self, speed=50):
        self._set_rhs_backward()
        self._set_lhs_backward()
        self.pwm1.start(speed)
        self.pwm2.start(speed)

    def turn_left(self):
        self._set_lhs_backward()
        self._set_rhs_forward()
        self.pwm1.start(100)
        self.pwm2.start(100)
        time.sleep(turning_duration)
        self.pause()

    def turn_right(self):
        self._set_rhs_backward()
        self._set_lhs_forward()
        self.pwm1.start(100)
        self.pwm2.start(100)
        time.sleep(turning_duration)
        self.pause()

    def pause(self):
        self._stop_lhs()
        self._stop_rhs()

    def stop(self):
        self.pause()
        self.pwm1.stop()
        self.pwm2.stop()

    def _set_lhs_forward(self):
        MOTOR1_DIRECTION_PIN_1.value(val=Pin.HIGH)
        MOTOR1_DIRECTION_PIN_2.value(val=Pin.LOW)

    def _set_lhs_backward(self):
        MOTOR1_DIRECTION_PIN_2.value(val=Pin.HIGH)
        MOTOR1_DIRECTION_PIN_1.value(val=Pin.LOW)

    def _stop_lhs(self):
        MOTOR1_DIRECTION_PIN_1.value(val=Pin.LOW)
        MOTOR1_DIRECTION_PIN_2.value(val=Pin.LOW)

    def _set_rhs_forward(self):
        MOTOR2_DIRECTION_PIN_1.value(val=Pin.HIGH)
        MOTOR2_DIRECTION_PIN_2.value(val=Pin.LOW)

    def _set_rhs_backward(self):
        MOTOR2_DIRECTION_PIN_2.value(val=Pin.HIGH)
        MOTOR2_DIRECTION_PIN_1.value(val=Pin.LOW)

    def _stop_rhs(self):
        MOTOR2_DIRECTION_PIN_1.value(val=Pin.LOW)
        MOTOR2_DIRECTION_PIN_2.value(val=Pin.LOW)
