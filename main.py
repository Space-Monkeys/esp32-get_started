import time
from machine import Pin

led = Pin(2, Pin.OUT)


while True:
    led.value(1)
    time.sleep(0.5)
    led.value(0)
    time.sleep(0.5)
