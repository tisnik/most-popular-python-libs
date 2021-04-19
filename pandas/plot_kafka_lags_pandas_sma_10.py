#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_kafka_lags_pandas_sma_10.py input_file.csv")
    print("Example:")
    print("  plot_kafka_lags_pandas_sma_10.py overall.csv")
    sys.exit(1)

# First command line argument should contain name of input CSV.
input_csv = sys.argv[1]

df = pd.read_csv(input_csv)

df['SMA_20'] = df.iloc[:, 1].rolling(window=20).mean()

print(df)
print(df.info())
print(df.describe())

# Create new histogram graph
df.plot(x="Time", y=["topic : uploads", "SMA_20"])

# Try to show the plot on screen
plt.show()

# Create new histogram graph
df.plot(x="Time", y="SMA_20")

# Try to show the plot on screen
plt.show()
