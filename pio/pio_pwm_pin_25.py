import time

import rp2
from machine import Pin


@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink6():
    pull(block)                # přečtení hodnoty z FIFO s čekáním, uložení do OSR
    mov(x, osr)                # přesun hodnoty z OSR do registru X
    wrap_target()              # cíl skoku
    pull(noblock)              # zkusíme přečíst novou poslanou hodnotu, ale nečekáme na ni
                               # pokud hodnota nebyla poslána, doplní se hodnota registru X
    mov(x, osr)                # přesun hodnoty z OSR do registru X
    set(y, 31)                 # počitadlo smyčky
    set(pins, 1)               # nastavit pin
    label("blink_loop")
    jmp(x_not_y, "skip")       # když X!=Y přeskočit další instrukci
    set(pins, 0)               # vynulovat pin
    label("skip")
    nop() [29]                 # zpožďovací mechanismus
    jmp(y_dec, "blink_loop")   # a opakujeme Y-krát
    wrap()


sm = rp2.StateMachine(0, blink6, freq=200000, set_base=Pin(25))
sm.active(1)                   # spustit stavový stroj

for duty_cycle in range(0, 32):
    time.sleep(0.3)
    sm.put(duty_cycle)         # prahová hodnota, která se pošle do FIFO

for duty_cycle in range(31, 0, -1):
    time.sleep(0.3)
    sm.put(duty_cycle)         # prahová hodnota, která se pošle do FIFO
