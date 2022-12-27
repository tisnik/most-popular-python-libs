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

from capstone import Cs, CS_ARCH_X86, CS_MODE_64


with open("loops.bin", "rb") as fin:
    code = fin.read()

md = Cs(CS_ARCH_X86, CS_MODE_64)
for i in md.disasm(code, 0x0000):
    print("0x%x:\t%s\t%s" % (i.address, i.mnemonic, i.op_str))
