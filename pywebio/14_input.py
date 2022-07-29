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
