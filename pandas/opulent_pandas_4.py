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

"""Reading CSV file that contains column with integer values (some are missing)."""


from opulent_pandas import BaseValidator, Error, Required, Schema

import numpy as np
import pandas


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


class IntOrNAValidator(BaseValidator):
    def validate(self, values):
        for value in values:
            if type(value) == np.int64:
                return
            if not (pandas.isna(value)):
                raise Error("Int value or NA expected")


def validate_data_frame(data_frame):

    schema = Schema(
        {
            Required("Block size"): [PosintValidator()],
            Required("Time to read"): [IntOrNAValidator()],
        }
    )

    schema.validate(data_frame)


df = pandas.read_csv("missing_integer_values.csv", dtype={"Time to read": "Int64"})
print_data_frame(df)
validate_data_frame(df)
