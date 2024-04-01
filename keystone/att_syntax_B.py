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
from keystone import KS_ARCH_X86, KS_MODE_16, KS_OPT_SYNTAX_ATT, Ks, KsError

# instrukce, které se mají assemblerem přeložit
CODE = """
    MOV $64, %AX
    INC %AX
    MOV %AX, %BX
"""

try:
    # inicializace assembleru se specifikací architektury a popř. i režimu
    ks = Ks(KS_ARCH_X86, KS_MODE_16)

    # exlicitní specifikace použité syntaxe
    ks.syntax = KS_OPT_SYNTAX_ATT

    # vlastní překlad (assembling)
    encoding, count = ks.asm(CODE)

    # tisk výsledku činnosti assembleru
    print("%s = %s (number of statements: %u)" % (CODE, encoding, count))
except KsError as e:
    print("ERROR: %s" % e)
