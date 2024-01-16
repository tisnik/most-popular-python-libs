#
#  (C) Copyright 2022  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

# import všech symbolů assembleru použitých ve skriptu
# import všech symbolů disassembleru použitých ve skriptu
from capstone import CS_ARCH_X86, CS_MODE_64, Cs
from keystone import KS_ARCH_X86, KS_MODE_64, Ks, KsError

# instrukce, které se mají přeložit assemblerem
CODE = """
    MOV EBX, 10
OUTER_LOOP:
    MOV EAX, 100
INNER_LOOP:
    DEC EAX
    JNZ INNER_LOOP
    DEC EBX
    JNZ OUTER_LOOP
"""

try:
    # inicializace assembleru se specifikací architektury a popř. i režimu
    ks = Ks(KS_ARCH_X86, KS_MODE_64)

    # vlastní překlad (assembling)
    encoding, count = ks.asm(CODE)

    # disassembling binární sekvence kódů
    md = Cs(CS_ARCH_X86, CS_MODE_64)

    # vypsat podrobnější informace o každé instrukci
    for i in md.disasm(bytes(encoding), 0x1234):
        # převod pole bajtů na řetězec s hexa hodnotami
        dump = i.bytes.hex(" ")

        # výpis informací o instrukci
        print(
            "0x{:02x}:\t{:20s}\t{:s}\t{:s}".format(
                i.address, dump, i.mnemonic, i.op_str
            )
        )

except KsError as e:
    print("ERROR: %s" % e)
