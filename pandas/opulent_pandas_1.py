#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading CSV file that contains column with integer values (some are missing)."""


import pandas
import math
from opulent_pandas import Schema, TypeValidator, Required


def print_data_frame(df):
    print("Data frame")
    print("---------------------------")
    print(df)
    print()

    print("Column types")
    print("---------------------------")
    print(df.dtypes)


def validate_data_frame(data_frame):
    schema = Schema({
        Required('Block size'): [TypeValidator(int)],
        Required('Time to read'): [TypeValidator(int)],
        })

    schema.validate(data_frame)


df = pandas.read_csv("integer_values.csv")
print_data_frame(df)
validate_data_frame(df)
