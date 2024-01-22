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

cities = (
    "Praha",
    "Brno",
    "Ostrava",
    "Plzeň",
    "Liberec",
    "Olomouc",
    "České Budějovice",
    "Hradec Králové",
    "Ústí nad Labem",
    "Pardubice",
)


def check_postal_code(value):
    if value <= 10000:
        return "Neplatné PSČ - příliš malá hodnota"
    elif value > 99999:
        return "Neplatné PSČ - příliš velká hodnota"


def check_city(name):
    if name not in cities:
        return "Neznámé město"


# vstupní údaje
info = inp.input_group(
    "Adresa",
    [
        inp.input("Jméno", name="name", type=inp.TEXT),
        inp.input("Příjmení", name="surname", type=inp.TEXT),
        inp.input("Ulice", name="street", type=inp.TEXT),
        inp.input("ČP", name="conscription_number", type=inp.NUMBER),
        inp.input("Město", name="city", type=inp.TEXT, validate=check_city),
        inp.input(
            "PSČ", name="postal_code", type=inp.NUMBER, validate=check_postal_code
        ),
    ],
)

# výpis výsledků
out.put_info("Zakázka bude poslána na adresu")

out.put_row(
    [
        out.put_text(info["name"]),
        out.put_text(info["surname"]),
    ],
    size="30% 30%",
)

out.put_row(
    [
        out.put_text(info["street"]),
        out.put_text(info["conscription_number"]),
    ],
    size="30% 10%",
)

out.put_row(
    [
        out.put_text(info["postal_code"]),
        out.put_text(info["city"]),
    ],
    size="10% 20%",
)
