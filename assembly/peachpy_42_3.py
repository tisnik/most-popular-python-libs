# Základy použití knihovny PeachPy
#
# - vytvoření subrutiny vracející konstantu
# - optimalizovaná varianta


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

# obalení strojového kódu tak, aby se dal volat z interpretru Pythonu
function_42 = asm_function.finalize(abi.detect()).encode().load()

# typ hodnoty
print(type(function_42))
print()

# zavolání nové funkce
print(function_42())
