import time

from robocar.drive import DriveSystem
from robocar.sonar import setup, get_sonar


def loop():
    drive = DriveSystem()
    setup()

    drive.forwards()

    while True:
        obstacle_distance = get_sonar()
        if obstacle_distance != 0 and obstacle_distance < 10:
            print("obstacle detected")
            drive.turn_left()
            drive.forwards()
        time.sleep(0.1)


if __name__ == "__main__":
    print("starting... ")

    try:
        loop()
    except KeyboardInterrupt:
        print("stopping...")
