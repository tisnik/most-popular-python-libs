# Základy použití knihovny PeachPy
#
# - definice instrukce ADD s různými kombinacemi registrů
# - tisk strojového kódu této instrukce
# - tisk instrukce ve formátu Netwide Assembleru
# - tisk instrukce ve formátu PeachPy
# - tisk instrukce ve formátu GNU Assembleru
# - tisk instrukce ve formátu Go Assembleru


# registry
# konstruktory instrukcí
from peachpy.x86_64 import (
    ADD,
    r8,
    r9,
    r10,
    r11,
    r12,
    r13,
    r14,
    r15,
    rax,
    rbp,
    rbx,
    rcx,
    rdi,
    rdx,
    rsi,
)


def print_instruction(instruction):
    print(" ".join(format(byte, "02x") for byte in instruction.encode()), end="\t")
    print(instruction.format(assembly_format="peachpy"), end="\t")
    print(instruction.format(assembly_format="gas"))


for r1 in  rax, rbx, rcx, rdx, rsi, rdi, rbp, r8, r9, r10, r11, r12, r13, r14, r15:
    for r2 in  rax, rbx, rcx, rdx, rsi, rdi, rbp, r8, r9, r10, r11, r12, r13, r14, r15:
        print_instruction(ADD(r1, r2))
