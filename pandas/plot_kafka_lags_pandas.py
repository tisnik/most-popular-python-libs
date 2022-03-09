#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_kafka_lags_pandas.py input_file.csv")
    print("Example:")
    print("  plot_kafka_lags_pandas.py overall.csv")
    sys.exit(1)

# First command line argument should contain name of input CSV.
input_csv = sys.argv[1]

# Try to open the CSV file specified.
df = pd.read_csv(input_csv)

print(df.info())
print(df.describe())

# Linear regression
time = df["Time"]
messages = df["topic : uploads"]

# Linear regression
x = np.arange(0, len(messages))
coef = np.polyfit(x, messages, 1)
poly1d_fn = np.poly1d(coef)

# Create new histogram graph
plt.plot(messages, "b", poly1d_fn(np.arange(0, len(messages))), "y--")

# Title of a graph
plt.title("Messages in Kafka")

# Add a label to x-axis
plt.xlabel("Time")

# Add a label to y-axis
plt.ylabel("Messages")

plt.legend(loc="upper right")

# Set the plot layout
plt.tight_layout()

# And save the plot into raster format and vector format as well
plt.savefig("kafka_lags_pandas.png")
plt.savefig("kafka_lags_pandas.svg")

# Try to show the plot on screen
plt.show()
