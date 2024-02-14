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
def asr_operation(r0, r1):
    asr(r0, r1)


print(hex(asr_operation(-0x100, 0)))
print(hex(asr_operation(-0x100, 1)))
print(hex(asr_operation(-0x100, 2)))
print(hex(asr_operation(-0x100, 3)))
