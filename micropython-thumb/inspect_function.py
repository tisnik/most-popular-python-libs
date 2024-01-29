import machine
import array


def inspect(f, nbytes=16):
    baddr = bytes(array.array("O", [f]))
    addr = int.from_bytes(baddr, "little")
    print("function object at: 0x%08x" % addr)
    print("number of args: %u" % machine.mem32[addr + 4])
    code_addr = machine.mem32[addr + 8]
    print("machine code at: 0x%08x" % code_addr)
    print("-- code --")
    for i in range(nbytes):
        print(f"{machine.mem8[code_addr + i]:02x}", end=" ")
    print("\n----------")
