#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pywebio.input as inp
import pywebio.output as out


# Body Mass Index calculator

info = inp.input_group(
    "Entry",
    [inp.input("Mass (kg)", name="mass"), inp.input("Height (cm)", name="height")],
)

mass = float(info["mass"])
height = float(info["height"])

# převod výšky na metry
height = height / 100.0

# výpočet (bez jakýchkoli kontrol)
bmi = mass / (height * height)

# výpis výsledku
out.put_info("BMI = ", bmi)
