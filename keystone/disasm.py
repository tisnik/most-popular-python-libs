from capstone import *


with open("loops.bin", "rb") as fin:
    code = fin.read()

md = Cs(CS_ARCH_X86, CS_MODE_64)
for i in md.disasm(code, 0x0000):
    print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))
