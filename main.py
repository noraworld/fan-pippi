import time
from lib import cpu
from lib import fan
from lib import gpio

SLEEP_INTERVAL = 2

if __name__ == '__main__':
    motor = gpio.setup()

    try:
        while True:
            speed = fan.speed(cpu.temp())
            motor.start(speed)
            time.sleep(SLEEP_INTERVAL)

    except:
        motor.stop()
        gpio.cleanup()
