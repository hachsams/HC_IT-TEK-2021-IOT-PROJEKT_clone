import machine
import time
from machine import Pin

Pin(32, Pin.OUT, value=1)
time.sleep(1)
Pin(32, Pin.OUT, value=0)