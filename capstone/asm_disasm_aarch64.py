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
from keystone import Ks, KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN, KsError

# import všech symbolů disassembleru použitých ve skriptu
from capstone import Cs, CS_ARCH_ARM64, CS_MODE_LITTLE_ENDIAN


# instrukce, které se mají přeložit assemblerem
CODE = """
    MOV  W0, 10
OUTER_LOOP:
    MOV  W1, 100
INNER_LOOP:
    SUBS W1, W1, 1
    BNE  INNER_LOOP
    SUBS W0, W0, 1
    BNE  OUTER_LOOP
"""

try:
    # inicializace assembleru se specifikací architektury a popř. i režimu
    ks = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)

    # vlastní překlad (assembling)
    encoding, count = ks.asm(CODE)

    # disassembling binární sekvence kódů
    md = Cs(CS_ARCH_ARM64, CS_MODE_LITTLE_ENDIAN)

    # vypsat podrobnější informace o každé instrukci
    for i in md.disasm(bytes(encoding), 0x0000):
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
