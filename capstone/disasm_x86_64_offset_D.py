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
from capstone import Cs, CS_ARCH_X86, CS_MODE_64

# pozice v binárním souboru, od níž jsou instrukce uloženy
OFFSET = 1000

# otevřít binární soubor a přečíst jeho obsah
with open("loops_x.bin", "rb") as fin:
    code = fin.read()
    code = code[OFFSET:]

# disassembling obsahu binárního souboru
md = Cs(CS_ARCH_X86, CS_MODE_64)

# vypsat podrobnější informace o každé instrukci
for i in md.disasm(code, 1000):
    # převod pole bajtů na řetězec s hexa hodnotami
    dump = i.bytes.hex(" ")

    # výpis informací o instrukci
    print("0x{:02x}:\t{:20s}\t{:s}\t{:s}".format(i.address, dump, i.mnemonic, i.op_str))
