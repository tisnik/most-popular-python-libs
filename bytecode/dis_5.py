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
# Modul s nekolika jednoduchymi funkcemi
# pro otestovani zakladnich vlastnosti bajtkodu jazyka Python
# prekladu programove struktury typu if-then-else.
#


def prikaz1(x):
    if x:
        return 10
    else:
        return 20


def prikaz2(x, y):
    if x:
        if y:
            return 10
        else:
            return 20
    else:
        return 30


#
# Vse je nutne otestovat.
#
def main():
    print(prikaz1(True))
    print(prikaz1(False))
    print(prikaz2(True, True))
    print(prikaz2(True, False))
    print(prikaz2(False, True))
    print(prikaz2(False, False))


def disassemble():
    from dis import dis

    print("\nprikaz1:")
    dis(prikaz1)

    print("\nprikaz2:")
    dis(prikaz2)


main()

disassemble()
