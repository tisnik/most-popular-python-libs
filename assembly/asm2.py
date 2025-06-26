# Kombinace programovacího jazyka Python a assembleru
#
# - strojový kód zapsaný do bufferu
# - korektní nastavení přístupových práv ke sdílené paměti
# - konstrukce "céčkové" funkce z tohoto kódu (funkce bez parametrů)
# - obalení "céčkové" funkce kódem volatelným z Pythonu
# - otestování nové funkce

import ctypes
import mmap

# konstrukce bufferu
with mmap.mmap(-1, mmap.PAGESIZE, prot=mmap.PROT_WRITE | mmap.PROT_EXEC) as buffer:
    # zapis strojoveho kodu do bufferu
    buffer.write(
        b'\xB8\x2A\x00\x00\x00'
        b'\xC3'
    )

    # deklarace typu nativni funkce
    function_type = ctypes.CFUNCTYPE(ctypes.c_int)

    # ziskani adresy strojoveho kodu
    function_pointer = ctypes.c_void_p.from_buffer(buffer)

    # reference na volatelnou funkci
    function_42 = function_type(ctypes.addressof(function_pointer))

    # zavolani funkce a vypis vysledku
    result = function_42()
    print(result)

    # pred uzavrenim bufferu je nutne odstranit ukazatele
    del function_pointer
