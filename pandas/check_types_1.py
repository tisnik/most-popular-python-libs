#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading CSV file that contains column with integer values (some are missing)."""

import pandas
from voluptuous import Schema


def print_data_frame(df):
    """Print the whole data frame."""
    print("Data frame")
    print("---------------------------")
    print(df)
    print()

    print("Column types")
    print("---------------------------")
    print(df.dtypes)


def validate_item(schema, data):
    """Validate one item from data frame."""
    try:
        print("\n\n")
        print(schema)
        print(data)
        schema(data)
        print("pass")
    except Exception as e:
        print(e)


def validate_data_frame(data_frame):
    """Validate the whole data frame."""
    print()

    print("Validation")
    print("---------------------------")

    schema = Schema((int, int, float))

    for record in df.itertuples():
        validate_item(schema, record)


df = pandas.read_csv("missing_integer_values.csv")
print_data_frame(df)
validate_data_frame(df)
