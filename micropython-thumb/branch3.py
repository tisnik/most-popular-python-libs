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
def branch():
    mov(r0, 42)
    b(cil_skoku)
    label(skok_zpet)
    mov(r0, 99)
    b(skok_zpet)
    mov(r0, 1)
    label(cil_skoku)
