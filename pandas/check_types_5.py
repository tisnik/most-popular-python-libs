#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading CSV file that contains column with integer values (some are missing)."""


import pandas
import math
from voluptuous import Schema
from voluptuous import Invalid
from voluptuous import Any


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
        print("\n")
        # print(schema)
        print(data)
        schema(data._asdict())
        print("pass")
    except Exception as e:
        print(e)


def posint(value):
    if type(value) is not int or value <= 0:
        raise Invalid("positive integer value expected, but got {v} instead".format(v=value))


def posfloat(value):
    if type(value) is not float or value <= 0:
        raise Invalid("positive float value expected, but got {v} instead".format(v=value))


def validate_data_frame(data_frame):
    print()

    print("Validation")
    print("---------------------------")

    schema = Schema({
        "Index": int,
        "Year2020": posint,
        "Year2019": posint,
        "Change": Any(str, float),
        "Language": str,
        "Ratings": posfloat,
        "Changep": float,
        })

    for record in df.itertuples():
        validate_item(schema, record)


colnames = ("Year2020", "Year2019", "Change", "Language", "Ratings", "Changep")
df = pandas.read_csv("tiobe.tsv", sep="\t", names=colnames, header=1)
print_data_frame(df)
validate_data_frame(df)
