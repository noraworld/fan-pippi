import json

FAN_PIN = 14
PWM_FREQ = 25

def speed(temp):
    function = get(temp)
    slope = (function['max_speed'] - function['min_speed']) / (function['max_temperature'] - function['min_temperature'])
    intercept = (function['max_temperature'] * function['min_speed'] - function['min_temperature'] * function['max_speed']) / (function['max_temperature'] - function['min_temperature'])
    speed = slope * temp + intercept

    debug({ "temp": temp, "speed": speed })

    return speed

def get(temp):
    file = open('fancontrol.json')
    data = json.load(file)
    file.close()

    for function in data['function']:
        if temp >= function['min_temperature'] and temp < function['max_temperature']:
            return function

def debug(item):
    for key, value in item.items():
        print(f'{key} = {value}')

    print()
