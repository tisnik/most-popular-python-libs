@micropython.asm_thumb
def loop():
    mov(r0, 0)
    mov(r1, 100)    # počáteční hodnota počitadla
    label(loop)     # označení začátku programové smyčky
    add(r0, r0, 4)  # tělo smyčky
    sub(r1, r1, 1)  # snížení hodnoty počitadla
    cmp(r1, 0)      # test na nulu
    bne(loop)       # skok v případě že se nedosáhlo nuly
