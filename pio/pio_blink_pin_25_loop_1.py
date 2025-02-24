import rp2
from machine import Pin


@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink1():
    set(x, 31)                 # počitadlo smyčky
    set(y, 16)                 # hraniční hodnota pro přepnutí pinu
    set(pins, 1)               # nastavit pin
    label("blink_loop")
    jmp(x_not_y, "skip")       # když x!=y přeskočit další instrukci
    set(pins, 0)               # vynulovat pin
    label("skip")
    nop() [29]                 # zpožďovací mechanismus
    jmp(x_dec, "blink_loop")   # a opakujeme x-krát


sm = rp2.StateMachine(0, blink1, freq=2000, set_base=Pin(25))
sm.active(1)                   # spustit stavový stroj
