from machine import Pin, Timer

led = Pin(8, Pin.OUT)
timer = Timer()

def blink(timer):
    led.toggle()

timer.init(freq=2, mode=Timer.PERIODIC, callback=blink)
