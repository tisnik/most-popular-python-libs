import rp2
from machine import Pin


@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink3():
    set(y, 16)                 # hraniční hodnota pro přepnutí pinu
    wrap_target()              # cíl skoku
    set(x, 31)                 # počitadlo smyčky
    set(pins, 1)               # nastavit pin
    label("blink_loop")
    jmp(x_not_y, "skip")       # když x!=y přeskočit další instrukci
    set(pins, 0)               # vynulovat pin
    label("skip")
    nop() [29]                 # zpožďovací mechanismus
    jmp(x_dec, "blink_loop")   # a opakujeme x-krát
    wrap()


sm = rp2.StateMachine(0, blink3, freq=2000, set_base=Pin(8))
sm.active(1)                   # spustit stavový stroj
