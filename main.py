import time
from lib import cpu
from lib import fan
from lib import gpio

if __name__ == '__main__':
    motor = gpio.setup()

    try:
        while True:
            temp = cpu.temp()
            speed = fan.speed(temp)
            motor.start(speed)
            time.sleep(fan.interval(temp))

    except:
        motor.stop()
        gpio.cleanup()
