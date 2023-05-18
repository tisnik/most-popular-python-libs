#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading CSV file that contains column with integer values (some are missing)."""

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

import pandas
from voluptuous import Schema
from voluptuous import Invalid


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


def pos(value):
    """Validate if the value is positive integer number."""
    if type(value) is not int or value <= 0:
        raise Invalid(
            "positive integer value expected, but got {v} instead".format(v=value)
        )


def validate_data_frame(data_frame):
    """Validate the whole data frame."""
    print()

    print("Validation")
    print("---------------------------")

    schema = Schema((pos, pos, float))

    for record in df.itertuples():
        validate_item(schema, record)


df = pandas.read_csv("missing_integer_values.csv")
print_data_frame(df)
validate_data_frame(df)
