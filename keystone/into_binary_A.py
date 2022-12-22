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

from keystone import *

# instrukce, které se mají assemblerem přeložit
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

    # uložení výsledného nativního kódu do souboru
    with open("loops.bin", "wb") as fout:
        fout.write(bytes(encoding))
except KsError as e:
    print("ERROR: %s" % e)
