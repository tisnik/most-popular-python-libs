from keystone import *

CODE = """
    MOV $64, %AX
    INC %AX
    MOV %AX, %BX
"""

try:
    ks = Ks(KS_ARCH_X86, KS_MODE_16)
    ks.syntax = KS_OPT_SYNTAX_ATT
    encoding, count = ks.asm(CODE)
    print("%s = %s (number of statements: %u)" % (CODE, encoding, count))
except KsError as e:
    print("ERROR: %s" % e)
