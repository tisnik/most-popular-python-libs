from array import array

control = array("I", [100000])


@micropython.asm_thumb
def return_big_constant(r0):
    ldr(r0, [r0, 0])

return_big_constant(control)
