#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pywebio.input as inp
import pywebio.output as out


# vstupní údaje
info = inp.input_group(
    "Adresa",
    [
        inp.input("Jméno", name="name"),
        inp.input("Příjmení", name="surname"),
        inp.input("Ulice", name="street"),
        inp.input("ČP", name="conscription_number"),
        inp.input("Město", name="city"),
        inp.input("PSČ", name="postal_code"),
    ],
)

# výpis výsledků
out.put_info("Zakázka bude poslána na adresu")

out.put_info(
    f"{info['name']} {info['surname']}\n{info['street']} {info['conscription_number']}\n{info['postal_code']} {info['city']}"
)
