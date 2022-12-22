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

try:
    # načtení kódu v assembleru ze souboru
    with open("hello_world_2.asm", "r") as fin:
        code = fin.read()

    # kontrolní výpis, jaký kód budeme překládat
    print(code)

    # inicializace assembleru se specifikací architektury a popř. i režimu
    ks = Ks(KS_ARCH_X86, KS_MODE_64)

    # vlastní překlad (assembling)
    encoding, count = ks.asm(code)

    # uložení výsledného nativního kódu do souboru
    with open("hello_2.bin", "wb") as fout:
        fout.write(bytes(encoding))
except KsError as e:
    print("ERROR: %s" % e)
