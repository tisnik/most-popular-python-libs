from keystone import *

try:
    with open("hello_world.asm", "r") as fin:
        code = fin.read()

    print(code)

    ks = Ks(KS_ARCH_X86, KS_MODE_64)
    encoding, count = ks.asm(code)
    with open("hello.bin", "wb") as fout:
        fout.write(bytes(encoding))
except KsError as e:
    print("ERROR: %s" % e)
