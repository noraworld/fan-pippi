import RPi.GPIO as GPIO

FAN_PIN = 14
PWM_FREQ = 25

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FAN_PIN, GPIO.OUT, initial = GPIO.LOW)

    return GPIO.PWM(FAN_PIN, PWM_FREQ)

def cleanup():
    GPIO.cleanup()
