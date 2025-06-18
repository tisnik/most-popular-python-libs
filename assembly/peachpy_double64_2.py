# Základy použití knihovny PeachPy
#
# - definice subrutiny double vracející dvojnásobnou hodnotu argumentu
# - korektní výpočty s 64bitovými hodnotami
# - tisk vytvořeného strojového kódu
# - otestování funkcionality této subrutiny


# datové typy
from peachpy import Argument, int64_t

# základní konstruktory atd.
# registry
# konstruktory instrukcí
from peachpy.x86_64 import ADD, MOV, RETURN, Function, abi, rax, rdi

x = Argument(int64_t)

# vytvoření nové subrutiny ve strojovém kódu
with Function("Function_double", (x, ), int64_t) as asm_function:
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

# přetečení 32bitové hodnoty se nekoná
print(double(10000000000))
