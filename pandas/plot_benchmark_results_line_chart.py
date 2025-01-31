#!/usr/bin/env python3

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

import sys

import matplotlib.pyplot as plt
import pandas as pd

# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_benchmark_results_line_chart.py ")
    print("Example:")
    print("  plot_benchmark_results_line_chart.py data.tsv")
    sys.exit(1)

# First command line argument should contain name of input CSV.
input_file = sys.argv[1]

df = pd.read_csv(input_file, sep="\t")

data_columns = [
    "ANSI C",
    "Cython #1",
    "Cython #2",
    "Cython #3",
    "Numba #1/interpret",
    "Numba #2",
    "Numba #3",
    "Numba #4",
]

for data_column in data_columns:
    df[data_column] = pd.to_numeric(
        df[data_column].str.replace(",", "."), errors="coerce"
    )

print(df)
print()

print(df.info())
print()

print(df.describe())
print()


# Create new histogram graph
df.plot(x="Height", y=data_columns)

# Try to show the plot on screen
plt.show()
