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
out.put_text("Jméno")
name = inp.input()

out.put_text("Příjmení")
surname = inp.input()

out.put_text("Ulice")
street = inp.input()

out.put_text("ČP")
conscription_number = inp.input()

out.put_text("Město")
city = inp.input()

out.put_text("PSČ")
postal_code = inp.input()

# výpis výsledků
out.put_info("Zakázka bude poslána na adresu")

out.put_info(f"{name} {surname}\n{street} {conscription_number}\n{postal_code} {city}")
