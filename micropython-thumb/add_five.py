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
def add_four(r0, r1, r2, r3, r4):
    add(r0, r0, r1)
    add(r0, r0, r2)
    add(r0, r0, r3)
    add(r0, r0, r4)
