#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading CSV with custom timestamps format using custom parser."""

import pandas
import datetime


def datetime_parser(raw_data):
    return datetime.datetime.strptime(raw_data, "%Y/%m/%d %H-%M-%S")


df = pandas.read_csv("custom_timestamps.csv",
                     date_parser=lambda raw_data: datetime.datetime.strptime(raw_data, "%Y/%m/%d %H-%M-%S"),
                     parse_dates=["Timestamp"])


pandas.to_datetime(df.Timestamp)

print("Data frame")
print("---------------------------")
print(df)
print()

print("Column types")
print("---------------------------")
print(df.dtypes)
