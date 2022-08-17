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

import symtable


with open("sprites.py") as fin:
    code = fin.read()
    t = symtable.symtable(code, "sprites.py", "exec")

print("Symbol table:", t)
print("Type:", t.get_type())
print("Has children:", t.has_children())
print("Identifiers:", t.get_identifiers())

symbols = t.get_symbols()

print("\nList of symbols:")

for symbol in symbols:
    print(symbol.get_name())
