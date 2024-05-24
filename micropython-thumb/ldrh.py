from array import array

control = array("B", [255, 255, 100, 0, 255, 255])


@micropython.asm_thumb
def load_halfword(r0):
    mov(r1, 1)
    mvn(r1, r1)  # nyni bude R1 obsahovat same jednicky
    ldrh(r1, [r0, 2])
    mov(r0, r1)


load_halfword(control)
