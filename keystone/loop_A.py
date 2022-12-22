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
    MOV EAX, 100
LOOP:
    DEC EAX
    JNZ LOOP
"""

try:
    # inicializace assembleru se specifikací architektury a popř. i režimu
    ks = Ks(KS_ARCH_X86, KS_MODE_64)

    # vlastní překlad (assembling)
    encoding, count = ks.asm(CODE)

    # tisk výsledku činnosti assembleru
    print("%s = %s (number of statements: %u)" % (CODE, encoding, count))
except KsError as e:
    print("ERROR: %s" % e)
