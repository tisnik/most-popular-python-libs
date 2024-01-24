@micropython.asm_thumb
def inc(r0):
    mov(r1, 1)
    add(r0, r0, r1)
