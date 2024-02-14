#
#  (C) Copyright 2024  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

@micropython.asm_thumb
def and_operation(r0, r1):
    and_(r0, r1)


print(hex(and_operation(0x00, 0x00)))
print(hex(and_operation(0xff, 0xaa)))
print(hex(and_operation(0x18, 0xf0)))
print(hex(and_operation(0x18, 0x0f)))
