@micropython.asm_thumb
def inc(x):
    mov(r1, 1)
    add(r0, r0, r1)
