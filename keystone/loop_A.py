from keystone import *

CODE = """
LOOP:
    MOV EAX, 100
    DEC EAX
    JNZ LOOP
"""

try:
    ks = Ks(KS_ARCH_X86, KS_MODE_64)
    encoding, count = ks.asm(CODE)
    print("%s = %s (number of statements: %u)" % (CODE, encoding, count))
except KsError as e:
    print("ERROR: %s" % e)
