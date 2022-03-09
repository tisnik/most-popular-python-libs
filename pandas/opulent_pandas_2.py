#!/usr/bin/env python3
# vim: set fileencoding=utf-8

"""Reading CSV file that contains column with integer values (some are missing)."""


import pandas
from opulent_pandas import Schema, Required, BaseValidator, Error


def print_data_frame(df):
    print("Data frame")
    print("---------------------------")
    print(df)
    print()

    print("Column types")
    print("---------------------------")
    print(df.dtypes)


class PosintValidator(BaseValidator):
    def validate(self, values):
        if not (values > 0).all():
            raise Error("positive integer value expected")


def validate_data_frame(data_frame):

    schema = Schema(
        {
            Required("Block size"): [PosintValidator()],
            Required("Time to read"): [PosintValidator()],
        }
    )

    schema.validate(data_frame)


df = pandas.read_csv("integer_values.csv")
print_data_frame(df)
validate_data_frame(df)
