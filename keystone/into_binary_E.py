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

# import všech symbolů použitých ve skriptu
from keystone import Ks, KS_ARCH_MIPS, KS_MODE_MIPS32, KsError



# instrukce, které se mají přeložit assemblerem
CODE = """
        addiu   $sp,$sp,-8
        sw      $fp,4($sp)
        move    $fp,$sp
        sw      $4,8($fp)
        sw      $5,12($fp)
        lw      $3,8($fp)
        lw      $2,12($fp)
        nop
        addu    $2,$3,$2
        move    $sp,$fp
        lw      $fp,4($sp)
        addiu   $sp,$sp,8
        jr      $31
        nop
"""

try:
    # inicializace assembleru se specifikací architektury a popř. i režimu
    ks = Ks(KS_ARCH_MIPS, KS_MODE_MIPS32)

    # vlastní překlad (assembling)
    encoding, count = ks.asm(CODE)



    # uložení výsledného nativního kódu do souboru
    with open("mips.bin", "wb") as fout:
        fout.write(bytes(encoding))
    print("Binary file written")
except KsError as e:
    print("ERROR: %s" % e)
