@micropython.asm_thumb
def branch():
    mov(r0, 42)
    b(cil_skoku)
    mov(r0, 99)
    mov(r0, 0)
    mov(r0, 1)
    label(cil_skoku)
