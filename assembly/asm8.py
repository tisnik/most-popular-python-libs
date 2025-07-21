# Kombinace programovacího jazyka Python a assembleru
#
# - strojový kód zapsaný v hexadecimálním formátu přímo v Pythonu
# - korektní nastavení přístupových práv ke sdílené paměti
# - konstrukce "céčkové" funkce z tohoto kódu (funkce se dvěma parametry)
# - obalení "céčkové" funkce kódem volatelným z Pythonu
# - otestování nové funkce

import ctypes
import mmap

asm_src = """
     1                                  [bits 64]
     2                                  
     3 00000000 89F8                            mov eax, edi
     4 00000002 01F0                            add eax, esi
     5 00000004 C3                              ret
"""

machine_code = bytearray()
for line in asm_src.split("\n"):
    instruction_bytes = line[16:32]
    instruction_code = bytearray.fromhex(instruction_bytes)
    machine_code.extend(instruction_code)


print(machine_code)

# konstrukce bufferu
with mmap.mmap(-1, mmap.PAGESIZE, prot=mmap.PROT_WRITE | mmap.PROT_EXEC) as buffer:
    # zapis strojoveho kodu do bufferu
    buffer.write(machine_code)

    # deklarace typu nativni funkce
    function_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

    # ziskani adresy strojoveho kodu
    function_pointer = ctypes.c_void_p.from_buffer(buffer)

    # reference na volatelnou funkci
    add = function_type(ctypes.addressof(function_pointer))

    # zavolani funkce a vypis vysledku
    result = add(123, 456)
    print(result)

    # pred uzavrenim bufferu je nutne odstranit ukazatele
    del function_pointer
