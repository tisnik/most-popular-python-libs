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
from keystone import Ks, KS_ARCH_X86, KS_MODE_32, KsError

try:
    with open("subroutines.asm", "r") as fin:
        code = fin.read()

    print(code)

    ks = Ks(KS_ARCH_X86, KS_MODE_32)
    encoding, count = ks.asm(code)
    with open("subroutines.bin", "wb") as fout:
        fout.write(bytes(encoding))
    print("Binary file written")
except KsError as e:
    print("ERROR: %s" % e)
