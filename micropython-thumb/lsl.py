@micropython.asm_thumb
def lsl_operation(r0, r1):
    lsl(r0, r1)


print(hex(lsl_operation(0x01, 0)))
print(hex(lsl_operation(0x01, 1)))
print(hex(lsl_operation(0x01, 2)))
print(hex(lsl_operation(0x01, 3)))
