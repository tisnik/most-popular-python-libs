from array import array

control = array('B', [255, 255, 100, 255, 255])


@micropython.asm_thumb
def load_byte(r0):
    mov(r1, 1)
    mvn(r1, r1)  # nyni bude R1 obsahovat same jednicky
    ldrb(r1, [r0, 2])
    mov(r0, r1)


load_byte(control)
