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

"""Reading CSV with custom timestamps format using custom parser."""

import pandas
import datetime


df = pandas.read_csv(
    "custom_timestamps.csv",
    date_parser=lambda raw_data: datetime.datetime.strptime(
        raw_data, "%Y/%m/%d %H-%M-%S"
    ),
    parse_dates=["Timestamp"],
)


pandas.to_datetime(df.Timestamp)

print("Data frame")
print("---------------------------")
print(df)
print()

print("Column types")
print("---------------------------")
print(df.dtypes)
