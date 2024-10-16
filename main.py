import machine
import time
led1 = machine.Pin(1, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)
led3 = machine.Pin(3, machine.Pin.OUT)

while True:
    time.sleep(1)
    led1.value(1)
    time.sleep(1)
    led1.value(0)

    time.sleep(1)
    led2.value(1)
    time.sleep(1)
    led2.value(0)

    time.sleep(1)
    led3.value(1)
    time.sleep(1)
    led3.value(0)