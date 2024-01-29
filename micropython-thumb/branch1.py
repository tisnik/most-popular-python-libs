@micropython.asm_thumb
def branch():
    mov(r0, 42)
    b(cil_skoku)
    mov(r0, 99)
    label(cil_skoku)
