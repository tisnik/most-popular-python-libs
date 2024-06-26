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


from voluptuous import Any, Invalid, Schema

import pandas


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
        print("\n")
        # print(schema)
        print(data)
        schema(data._asdict())
        print("pass")
    except Exception as e:
        print(e)


def posint(value):
    """Validate if the value is positive integer number."""
    if type(value) is not int or value <= 0:
        raise Invalid(
            "positive integer value expected, but got {v} instead".format(v=value)
        )


def posfloat(value):
    """Validate if the value is positive floating point number."""
    if type(value) is not float or value <= 0:
        raise Invalid(
            "positive float value expected, but got {v} instead".format(v=value)
        )


def validate_data_frame(data_frame):
    """Validate the whole data frame."""
    print()

    print("Validation")
    print("---------------------------")

    schema = Schema(
        {
            "Index": int,
            "_1": posint,
            "_2": posint,
            "Change": Any(str, float),
            "Language": str,
            "Ratings": posfloat,
            "Changep": float,
        }
    )

    for record in df.itertuples():
        validate_item(schema, record)


df = pandas.read_csv("tiobe.tsv", sep="\t")
print_data_frame(df)
validate_data_frame(df)
