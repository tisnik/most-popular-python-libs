@micropython.asm_thumb
def bic_operation(r0, r1):
    bic(r0, r1)


print(hex(bic_operation(0x00, 0x00)))
print(hex(bic_operation(0xff, 0xaa)))
print(hex(bic_operation(0x18, 0xf0)))
print(hex(bic_operation(0x18, 0x0f)))
