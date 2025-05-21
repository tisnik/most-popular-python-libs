import ctypes
import mmap

# konstrukce bufferu
with mmap.mmap(-1, mmap.PAGESIZE, prot=mmap.PROT_WRITE | mmap.PROT_EXEC) as buffer:
    with open("42.bin", "rb") as fin:
        buffer.write(fin.read())

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
