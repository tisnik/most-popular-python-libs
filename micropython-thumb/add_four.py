@micropython.asm_thumb
def add_four(r0, r1, r2, r3):
    add(r0, r0, r1)
    add(r0, r0, r2)
    add(r0, r0, r3)
