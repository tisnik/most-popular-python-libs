from keystone import *

CODE = """
    MOV %AX, 100
    INC %AX
    MOV %BX, %AX
"""

try:
    ks = Ks(KS_ARCH_X86, KS_MODE_16)
    ks.syntax = KS_OPT_SYNTAX_ATT
    encoding, count = ks.asm(CODE)
    print("%s = %s (number of statements: %u)" % (CODE, encoding, count))
except KsError as e:
    print("ERROR: %s" % e)
