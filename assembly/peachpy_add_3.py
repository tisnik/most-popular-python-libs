# Základy použití knihovny PeachPy
#
# - definice subrutiny add pro součet dvou 64bitových hodnot
# - použití pojmenovaných argumentů
# - odlišná práce s registry
# - tisk vytvořeného strojového kódu
# - otestování funkcionality této subrutiny


# datové typy
from peachpy import Argument, int64_t

# základní konstruktory atd.
# registry
# konstruktory instrukcí
from peachpy.x86_64 import (
    ADD,
    LOAD,
    MOV,
    RETURN,
    Function,
    GeneralPurposeRegister64,
    abi,
    rax,
)

x = Argument(int64_t)
y = Argument(int64_t)

# vytvoření nové subrutiny ve strojovém kódu
with Function("Function_add", (x, y), int64_t) as asm_function:
    reg_x = GeneralPurposeRegister64()
    reg_y = GeneralPurposeRegister64()

    LOAD.ARGUMENT(reg_x, x)
    LOAD.ARGUMENT(reg_y, y)
    ADD(reg_x, reg_y)
    MOV(rax, reg_x)
    RETURN()

# obalení strojového kódu tak, aby se dal volat z interpretru Pythonu
add = asm_function.finalize(abi.detect()).encode().load()

# typ hodnoty
print(type(add))
print()

# výpis disassemblovaného strojového kódu
print(asm_function.finalize(abi.detect()).format_code())
print()

# zavolání nové funkce
print(add(1, 2))

print(add(10000000000, 20000000000))
