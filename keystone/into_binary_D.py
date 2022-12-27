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
from keystone import Ks, KS_ARCH_X86, KS_MODE_64, KS_OPT_SYNTAX_ATT, KsError


try:
    # načtení kódu v assembleru ze souboru
    with open("att_syntax.asm", "r") as fin:
        code = fin.read()

    # kontrolní výpis, jaký kód budeme překládat
    print(code)

    # inicializace assembleru se specifikací architektury a popř. i režimu
    ks = Ks(KS_ARCH_X86, KS_MODE_64)

    # specifikace použité syntaxe
    ks.syntax = KS_OPT_SYNTAX_ATT

    # vlastní překlad (assembling)
    encoding, count = ks.asm(code)

    # uložení výsledného nativního kódu do souboru
    with open("att_syntax.bin", "wb") as fout:
        fout.write(bytes(encoding))
    print("Binary file written")
except KsError as e:
    print("ERROR: %s" % e)
