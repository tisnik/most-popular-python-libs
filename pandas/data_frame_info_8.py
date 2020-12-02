#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading data file with custom format. separator + skip rows specification."""

import pandas

df = pandas.read_csv("denni_kurz.txt", sep="|", skiprows=1)

df["kurz"] = pandas.to_numeric(df["kurz"].str.replace(',','.'), errors='coerce')

print(df.describe())
