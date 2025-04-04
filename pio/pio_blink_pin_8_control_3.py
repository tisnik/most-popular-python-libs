import rp2
from machine import Pin


@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink6():
    pull(block)                # přečtení hodnoty z FIFO s čekáním, uložení do OSR
    mov(x, osr)                # přesun hodnoty z OSR do registru X
    wrap_target()              # cíl skoku
    pull(noblock)              # zkusíme přečíst novou poslanou hodnotu, ale nečekáme na ni
                               # pokud hodnota nebyla poslána, doplní se hodnota registru X
    mov(x, osr)                #  přesun hodnoty z OSR do registru X
    set(y, 31)                 # počitadlo smyčky
    set(pins, 1)               # nastavit pin
    label("blink_loop")
    jmp(x_not_y, "skip")       # když X!=Y přeskočit další instrukci
    set(pins, 0)               # vynulovat pin
    label("skip")
    nop() [29]                 # zpožďovací mechanismus
    jmp(y_dec, "blink_loop")   # a opakujeme Y-krát
    wrap()


sm = rp2.StateMachine(0, blink6, freq=2000, set_base=Pin(8))
sm.active(1)                   # spustit stavový stroj
sm.put(10)                     # prahová hodnota, která se pošle do FIFO
