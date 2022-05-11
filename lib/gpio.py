from dotenv import load_dotenv
import os
import RPi.GPIO as GPIO

def setup():
    load_dotenv()
    fan_pin = int(os.getenv('FAN_PIN'))
    pwm_freq = int(os.getenv('PWM_FREQ'))

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(fan_pin, GPIO.OUT, initial = GPIO.LOW)

    return GPIO.PWM(fan_pin, pwm_freq)

def cleanup():
    GPIO.cleanup()
