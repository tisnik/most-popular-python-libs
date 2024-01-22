#!/usr/bin/env python3
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2021  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import pywebio.input as inp
import pywebio.output as out

# vstupní údaje
info = inp.input_group(
    "Adresa",
    [
        inp.input("Jméno", name="name", type=inp.TEXT),
        inp.input("Příjmení", name="surname", type=inp.TEXT),
        inp.input("Ulice", name="street", type=inp.TEXT),
        inp.input("ČP", name="conscription_number", type=inp.NUMBER),
        inp.input("Město", name="city", type=inp.TEXT),
        inp.input("PSČ", name="postal_code", type=inp.NUMBER),
    ],
)

# výpis výsledků
out.put_info("Zakázka bude poslána na adresu")

out.put_info(
    f"{info['name']} {info['surname']}\n{info['street']} {info['conscription_number']}\n{info['postal_code']} {info['city']}"
)
