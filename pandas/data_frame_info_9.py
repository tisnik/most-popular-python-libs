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

"""Reading data file with custom format. separator + skip rows specification."""

import pandas

df = pandas.read_csv("denni_kurz.txt", sep="|", skiprows=1)

df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(",", "."), errors="coerce")

print(df.describe().info())
