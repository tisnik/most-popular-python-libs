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
# prekladu programove smycky typu while pri
# vypoctu rady prvocisel.
#
 
def primeNumbers(min, max):
    i = min
    while(i <= max):       # projit vsechny hodnoty od min do max
        j = 2
        while(j < i):      # (lze optimalizovat a zkratit smycku!)
            if i % j == 0: # je mozne celociselne delit?
                break      # - pak ovsem nejde o prvocislo
            j = j + 1      # vyzkouset dalsiho kandidata na celociselne deleni
        if (j == i):       # pokud jsme dosli az k cislu i
            print(i)       # nedoslo nikdy k celociselnemu deleni
        i = i + 1          # dalsi hodnota v posloupnosti
 
#
# Vse je nutne otestovat.
#
def main():
    primeNumbers(2, 1000)
 
def disassemble():
    from dis import dis
 
    print("\nprimeNumbers:")
    dis(primeNumbers)
 
main()
 
disassemble()
