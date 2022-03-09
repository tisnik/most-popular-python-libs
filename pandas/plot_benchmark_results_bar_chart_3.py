#!/usr/bin/env python3

import sys
import pandas as pd
import matplotlib.pyplot as plt

# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_benchmark_results.py ")
    print("Example:")
    print("  plot_benchmark_results.py data.tsv")
    sys.exit(1)

# First command line argument should contain name of input CSV.
input_file = sys.argv[1]

df = pd.read_csv(input_file, sep="\t")

df = df[10:]
data_columns = df.columns[1:]

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
df.plot.bar(x=df.columns[0], y=data_columns)

# Try to show the plot on screen
plt.show()
