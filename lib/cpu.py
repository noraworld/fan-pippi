from vcgencmd import Vcgencmd

def temp():
    vcgm = Vcgencmd()
    temp = vcgm.measure_temp()
    return temp
