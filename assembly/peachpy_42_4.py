# datové typy
from peachpy import int32_t

# základní konstruktory atd.
from peachpy.x86_64 import Function, GeneralPurposeRegister32, abi

# registry
from peachpy.x86_64 import eax

# konstruktory instrukcí
from peachpy.x86_64 import MOV, RETURN

# vytvoření nové subrutiny ve strojovém kódu
with Function("Function_42", (), int32_t) as asm_function:
    MOV(eax, 42)
    RETURN()


# výpis disassemblovaného strojového kódu
print(asm_function.finalize(abi.detect()).format_code())
