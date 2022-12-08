# asmsyntax=as

# Jednoducha aplikace typu "Hello world!" naprogramovana
# v assembleru GNU as - pouzita je "Intel" syntaxe.
#
# Autor: Pavel Tisnovsky

.intel_syntax noprefix


# Linux kernel system call table
sys_exit=1
sys_write=4


hello_lbl:
        .string "Hello World!\n"     # string, ktery JE ukoncen nulou


_start:
        mov   eax, sys_write         # cislo syscallu pro funkci "write"
        mov   ebx, 1                 # standardni vystup
        mov   ecx, hello_lbl         # adresa retezce, ktery se ma vytisknout
        mov   edx, 13                # pocet znaku, ktere se maji vytisknout
        int   0x80                   # volani Linuxoveho kernelu

        mov   eax, sys_exit          # cislo sycallu pro funkci "exit"
        mov   ebx, 0                 # exit code = 0
        int   0x80                   # volani Linuxoveho kernelu
