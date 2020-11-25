#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading CSV file that contains column with integer values (some are missing)."""


import pandas
import math
from voluptuous import Schema
from voluptuous import Invalid


def print_data_frame(df):
    print("Data frame")
    print("---------------------------")
    print(df)
    print()

    print("Column types")
    print("---------------------------")
    print(df.dtypes)


def validate_item(schema, data):
    try:
        print("\n\n")
        print(schema)
        print(data)
        schema(data)
        print("pass")
    except Exception as e:
        print(e)


def pos(value):
    if type(value) is not int or value <= 0:
        raise Invalid("positive integer value expected, but got {v} instead".format(v=value))


def nnat(value):
    if type(value) is not float or math.isnan(value):
        raise Invalid("non-NaN value expected, but got {v} instead".format(v=value))


def validate_data_frame(data_frame):
    print()

    print("Validation")
    print("---------------------------")

    schema = Schema((pos, pos, nnat))

    for record in df.itertuples():
        validate_item(schema, record)


df = pandas.read_csv("missing_integer_values.csv")
print_data_frame(df)
validate_data_frame(df)
