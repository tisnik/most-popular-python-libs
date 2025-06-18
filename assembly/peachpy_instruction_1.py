# Základy použití knihovny PeachPy
#
# - definice instrukce
# - tisk strojového kódu této instrukce
# - tisk instrukce ve formátu Netwide Assembleru
# - tisk instrukce ve formátu PeachPy
# - tisk instrukce ve formátu GNU Assembleru
# - tisk instrukce ve formátu Go Assembleru


# registry
# konstruktory instrukcí
from peachpy.x86_64 import ADD, rax, rdi


def print_instruction(instruction):
    print(" ".join(format(byte, "02x") for byte in instruction.encode()))
    print(instruction.format(assembly_format="nasm"))
    print(instruction.format(assembly_format="peachpy"))
    print(instruction.format(assembly_format="gas"))
    print(instruction.format(assembly_format="go"))


print_instruction(ADD(rax, rdi))
