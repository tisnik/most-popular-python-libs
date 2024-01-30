@micropython.asm_thumb
def loop():
    mov(r0, 0)
    mov(r1, 101)    # počáteční hodnota počitadla + 1
    label(loop)     # označení začátku programové smyčky
    sub(r1, r1, 1)  # snížení hodnoty počitadla + nastavení příznaků
    beq(break_loop) # skok v případě že se dosáhlo nuly
    add(r0, r0, 4)  # tělo smyčky
    b(loop)
    label(break_loop)
