#!/usr/bin/python
# vim: set fileencoding=utf-8

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

#
# Modul s jedinou funkci pro otestovani
# zakladnich vlastnosti bajtkodu jazyka Lua
# prekladu programove smycky typu while.
#

def loop(x):
    while x > 0:
        x = x - 1
    return x


#
# Vse je nutne otestovat.
#
def main():
    print(loop(10))

#
# Vypsani bajkkodu testovane funkce
#
def disassemble():
    from dis import dis

    print("\nloop:")
    dis(loop)

main()

disassemble()
