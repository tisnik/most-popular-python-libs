#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading CSV with timestamps with parsing."""

import pandas

df = pandas.read_csv("timestamps.csv", parse_dates=["Timestamp"])

print("Data frame")
print("---------------------------")
print(df)
print()

print("Column types")
print("---------------------------")
print(df.dtypes)
