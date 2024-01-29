@micropython.asm_thumb
def loop_mul():
    mov(r0, 10)
    mov(r1, 100)        # počáteční hodnota počitadla vnější smyčky
    label(outer_loop)   # označení začátku vnější programové smyčky
    mov(r2, 100)        # počáteční hodnota počitadla vnitřní smyčky
    label(inner_loop)   # označení začátku vnitřní programové smyčky
    mul(r0, r0)         # tělo smyčky
    sub(r2, r2, 1)      # snížení hodnoty počitadla + nastavení příznaků
    bne(inner_loop)     # opakování vnitřní smyčky
    sub(r1, r1, 1)      # snížení hodnoty počitadla + nastavení příznaků
    bne(outer_loop)     # opakování vnější smyčky


import utime
t1 = utime.ticks_us()
loop_mul()
t2 = utime.ticks_us()
print(utime.ticks_diff(t2, t1))
