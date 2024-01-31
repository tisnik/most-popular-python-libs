@micropython.asm_thumb
def asr_operation(r0, r1):
    asr(r0, r1)


print(hex(asr_operation(-0x100, 0)))
print(hex(asr_operation(-0x100, 1)))
print(hex(asr_operation(-0x100, 2)))
print(hex(asr_operation(-0x100, 3)))
