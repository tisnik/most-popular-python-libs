@micropython.asm_thumb
def lsr_operation(r0, r1):
    lsr(r0, r1)


print(hex(lsr_operation(0x100, 0)))
print(hex(lsr_operation(0x100, 1)))
print(hex(lsr_operation(0x100, 2)))
print(hex(lsr_operation(0x100, 3)))
