@micropython.asm_thumb
def ror_operation(r0, r1):
    ror(r0, r1)


print(hex(ror_operation(1, -3)))
print(hex(ror_operation(1, -2)))
print(hex(ror_operation(1, -1)))
print(hex(ror_operation(1, 0)))
print(hex(ror_operation(1, 1)))
print(hex(ror_operation(1, 2)))
print(hex(ror_operation(1, 3)))
