@micropython.asm_thumb
def or_operation(r0, r1):
    orr(r0, r1)


print(hex(or_operation(0x00, 0x00)))
print(hex(or_operation(0xff, 0xaa)))
print(hex(or_operation(0x18, 0xf0)))
print(hex(or_operation(0x18, 0x0f)))
