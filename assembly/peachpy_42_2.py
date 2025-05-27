# Základy použití knihovny PeachPy
#
# - vytvoření subrutiny vracející konstantu
# - neoptimalizovaná varianta
# - tisk vytvořeného strojového kódu


# datové typy
from peachpy import int32_t

# základní konstruktory atd.
from peachpy.x86_64 import Function, GeneralPurposeRegister32, abi

# konstruktory instrukcí
from peachpy.x86_64 import MOV, RETURN

# vytvoření nové subrutiny ve strojovém kódu
with Function("Function_42", (), int32_t) as asm_function:
    reg_x = GeneralPurposeRegister32()
    MOV(reg_x, 42)
    RETURN(reg_x)

# výpis disassemblovaného strojového kódu
print(asm_function.finalize(abi.detect()).format_code())
