import time

from robocar.pins import SONAR_ECHO_PIN, SONAR_TRIGGER_PIN
from adafruit_blinka.microcontroller.tegra.t210.pin import Pin

MAX_DISTANCE = 220
timeOut = MAX_DISTANCE * 60


def pulse_in(timeOut):
    t0 = time.time()
    while SONAR_ECHO_PIN.value() != Pin.HIGH:
        if (time.time() - t0) > timeOut * 0.000001:
            return 0
    t0 = time.time()
    while SONAR_ECHO_PIN.value() == Pin.HIGH:
        if (time.time() - t0) > timeOut * 0.000001:
            return 0
    pulseTime = (time.time() - t0) * 1000000
    return pulseTime


def get_sonar():
    SONAR_TRIGGER_PIN.value(val=Pin.HIGH)
    time.sleep(0.00001)
    SONAR_TRIGGER_PIN.value(val=Pin.LOW)
    pingTime = pulse_in(timeOut)
    distance = pingTime * 340.0 / 2.0 / 10000.0
    return distance


def setup():
    SONAR_ECHO_PIN.init(mode=Pin.IN)
    SONAR_TRIGGER_PIN.init(mode=Pin.OUT)
