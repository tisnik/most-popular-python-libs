@micropython.asm_thumb
def and_operation(r0, r1):
    and_(r0, r1)


print(hex(and_operation(0x00, 0x00)))
print(hex(and_operation(0xff, 0xaa)))
print(hex(and_operation(0x18, 0xf0)))
print(hex(and_operation(0x18, 0x0f)))
