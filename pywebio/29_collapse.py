#!/usr/bin/env python3
# vim: set fileencoding=utf-8

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

with out.put_collapse("Jméno a příjmení"):
    out.put_row(
        [
            out.put_text(info["name"]).style("color:red"),
            out.put_text(info["surname"]).style("color:red"),
        ],
        size="30% 30%",
    )

with out.put_collapse("Adresa"):
    out.put_row(
        [
            out.put_text(info["street"]).style("font-size:75%"),
            out.put_text(info["conscription_number"]).style("font-size:75%"),
        ],
        size="30% 10%",
    )

    out.put_row(
        [
            out.put_text(info["postal_code"]),
            out.put_text(info["city"]),
        ],
        size="10% 20%",
    ).style("background-color:#ccffcc")
