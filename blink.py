import time
from machine import Pin

print("Hello World")
p2 = Pin(2,Pin.OUT)

while True:
    p2.on()
    time.sleep_ms(500)
    p2.off()
    time.sleep_ms(500)
