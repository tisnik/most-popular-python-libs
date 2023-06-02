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

import pandas
import pprint

# přečtení zdrojových dat s jejich konverzí do datového rámce
df = pandas.read_csv("git_log.txt", sep="|")

# datový rámec zobrazíme
print(df)
print()

# rozdělení do skupin podle autora (jednoho sloupce)
gb = df.groupby(["Author"])

# zobrazení skupin vytvořených v rámci předchozího kroku
print("Group by author")
pprint.pprint(gb.groups)

# zobrazení počtu skupin
print()
print("Number of groups:", len(gb))
