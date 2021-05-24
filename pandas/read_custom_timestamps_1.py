#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading CSV with custom timestamps format."""

import pandas

df = pandas.read_csv("custom_timestamps.csv", parse_dates=["Timestamp"])

pandas.to_datetime(df.Timestamp)

print("Data frame")
print("---------------------------")
print(df)
print()

print("Column types")
print("---------------------------")
print(df.dtypes)
