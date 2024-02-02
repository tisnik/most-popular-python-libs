import array

import machine


def inspect(f):
    baddr = bytes(array.array("O", [f]))
    addr = int.from_bytes(baddr, "little")
    print("function object at: 0x%08x" % addr)
    print("number of args:     %u" % machine.mem32[addr + 4])
    code_addr = machine.mem32[addr + 8]
    print("machine code at:    0x%08x" % code_addr)

    previous = -1
    size = 0
    while True:
        current = machine.mem8[code_addr + size]
        size += 1
        if current == 0xbd and previous == 0xf2:
            break
        previous = current

    print(f"machine code size:  {size} bytes")

    print("-- code --")
    for i in range(size):
        print(f"{machine.mem8[code_addr + i]:02x}", end=" ")

    print("\n----------")
