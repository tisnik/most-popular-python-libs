# Základy použití knihovny PeachPy
#
# - definice subrutiny double vracející dvojnásobnou hodnotu argumentu
# - pokus o výpočty s 64bitovými hodnotami
# - tisk vytvořeného strojového kódu
# - otestování funkcionality této subrutiny


# datové typy
from peachpy import int64_t, Argument

# základní konstruktory atd.
from peachpy.x86_64 import Function, GeneralPurposeRegister32, abi

# registry
from peachpy.x86_64 import rax, rdi

# konstruktory instrukcí
from peachpy.x86_64 import ADD, MOV, RETURN

# vytvoření nové subrutiny ve strojovém kódu
with Function("Function_double", (), int64_t) as asm_function:
    MOV(rax, rdi)
    ADD(rax, rax)
    RETURN()

# obalení strojového kódu tak, aby se dal volat z interpretru Pythonu
double = asm_function.finalize(abi.detect()).encode().load()

# typ hodnoty
print(type(double))
print()

# výpis disassemblovaného strojového kódu
print(asm_function.finalize(abi.detect()).format_code())
print()

# zavolání nové funkce
print(double(42))

# přetečení 32bitové hodnoty se nekoná - nebo snad ano?
print(double(10000000000))
