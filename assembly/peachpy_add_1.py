# Základy použití knihovny PeachPy
#
# - definice subrutiny add pro součet dvou 64bitových hodnot
# - tisk vytvořeného strojového kódu
# - otestování funkcionality této subrutiny


# datové typy
from peachpy import int64_t, Argument

# základní konstruktory atd.
from peachpy.x86_64 import Function, GeneralPurposeRegister32, abi

# registry
from peachpy.x86_64 import rax, rdi, rsi

# konstruktory instrukcí
from peachpy.x86_64 import ADD, MOV, RETURN

x = Argument(int64_t)
y = Argument(int64_t)

# vytvoření nové subrutiny ve strojovém kódu
with Function("Function_add", (x, y), int64_t) as asm_function:
    MOV(rax, rdi)
    ADD(rax, rsi)
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
