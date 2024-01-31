@micropython.asm_thumb
def mvn_operation(r0):
    mvn(r0, r0)


print(hex(mvn_operation(0x00)))
print(hex(mvn_operation(0xff)))
print(hex(mvn_operation(0x18)))
print(hex(mvn_operation(0x0f)))
