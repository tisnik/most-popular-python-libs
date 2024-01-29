@micropython.asm_thumb
def branch():
    mov(r0, 42)
    b(cil_skoku)
    label(skok_zpet)
    mov(r0, 99)
    b(skok_zpet)
    mov(r0, 1)
    label(cil_skoku)
