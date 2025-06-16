# Základy použití knihovny PeachPy
#
# - vytvoření subrutiny vracející konstantu
# - optimalizovaná varianta
# - tisk vytvořeného strojového kódu


# datové typy
from peachpy import int32_t

# základní konstruktory atd.
# registry
# konstruktory instrukcí
from peachpy.x86_64 import MOV, RETURN, Function, abi, eax

# vytvoření nové subrutiny ve strojovém kódu
with Function("Function_42", (), int32_t) as asm_function:
    MOV(eax, 42)
    RETURN()


# výpis disassemblovaného strojového kódu
print(asm_function.finalize(abi.detect()).format_code())
