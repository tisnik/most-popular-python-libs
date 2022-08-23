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
# prekladu relacnich vyrazu.
#
 
def vyraz1(x, y):
    result = x <= y
    return result
 
def vyraz2(x, y):
    result = x < y
    return result
 
def vyraz3(x, y):
    result = x == y
    return result
 
def vyraz4(x, y):
    result = x != y
    return result
 
def vyraz5(x, y):
    result = x >= y
    return result
 
def vyraz6(x, y):
    result = x > y
    return result
 
 
#
# Vse je nutne otestovat.
#
def main():
    print(vyraz1(1, 2))
    print(vyraz2(1, 2))
    print(vyraz3(1, 2))
    print(vyraz4(1, 2))
    print(vyraz5(1, 2))
    print(vyraz6(1, 2))
 
def disassemble():
    from dis import dis
 
    print("\nvyraz1:")
    dis(vyraz1)
 
    print("\nvyraz2:")
    dis(vyraz2)
 
    print("\nvyraz3:")
    dis(vyraz3)
 
    print("\nvyraz4:")
    dis(vyraz4)
 
    print("\nvyraz5:")
    dis(vyraz5)
 
    print("\nvyraz6:")
    dis(vyraz6)
 
main()
 
disassemble()
