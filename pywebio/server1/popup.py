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


def main():
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
    out.popup(
        "Odeslání zakázky",
        [
            out.put_html("<h3>Odeslání zakázky</h3>"),
            out.put_info("Zakázka bude poslána na adresu"),
            out.put_info(
                f"{info['name']} {info['surname']}\n{info['street']} {info['conscription_number']}\n{info['postal_code']} {info['city']}"
            ),
            out.put_buttons(["OK"], onclick=lambda _: close_popup()),
        ],
    )
