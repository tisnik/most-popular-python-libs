#!/usr/bin/env python3
# vim: set fileencoding=utf-8

import pywebio.input as inp
import pywebio.output as out


# Body Mass Index calculator

out.put_text("Mass (kg): ")
mass = int(inp.input())

out.put_text("Height (cm): ")
height = int(inp.input())

# převod výšky na metry
height = height / 100.0

# výpočet (bez jakýchkoli kontrol)
bmi = mass / (height * height)

# výpis výsledku
out.put_info("BMI = ", bmi)
