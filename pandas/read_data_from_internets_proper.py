#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading data file from internets."""

import pandas

url = "https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
df = pandas.read_csv(url, sep="|", skiprows=1)

print("Data frame")
print("---------------------------")
print(df)
print()

print("Column types")
print("---------------------------")
print(df.dtypes)
