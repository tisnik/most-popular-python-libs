# Základy použití knihovny PeachPy
#
# - definice subrutiny double vracející dvojnásobnou hodnotu argumentu
# - použití pojmenovaných argumentů
# - tisk vytvořeného strojového kódu
# - otestování funkcionality této subrutiny


# datové typy
from peachpy import int32_t, Argument

# základní konstruktory atd.
from peachpy.x86_64 import Function, GeneralPurposeRegister32, abi

# registry
from peachpy.x86_64 import eax

# konstruktory instrukcí
from peachpy.x86_64 import ADD, MOV, LOAD, RETURN

x = Argument(int32_t)

# vytvoření nové subrutiny ve strojovém kódu
with Function("Function_double", (x, ), int32_t) as asm_function:
    LOAD.ARGUMENT(eax, x)
    ADD(eax, eax)
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

# přetečení 32bitové hodnoty
print(double(10000000000))
