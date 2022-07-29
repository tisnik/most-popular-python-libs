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
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_values_pandas.py input_file.csv")
    print("Example:")
    print("  plot_values_pandas.py overall.csv")
    sys.exit(1)

# First command line argument should contain name of input CSV.
input_csv = sys.argv[1]

# Try to open the CSV file specified.
df = pd.read_csv(input_csv)

# Print info about data frame
print(df.info())
print(df.describe())

# Linear regression
time = df["Time"]
messages = df["Value"]

# Linear regression
x = np.arange(0, len(messages))
coef = np.polyfit(x, messages, 1)
poly1d_fn = np.poly1d(coef)

# Create a figure containing a single axes.
fig, ax = plt.subplots()

# Create new graph
ax.plot(messages, "b", poly1d_fn(np.arange(0, len(messages))), "y--")

# Title of a graph
ax.set_title("Sensor values")

# Add a label to x-axis
ax.set_xlabel("Time")

# Add a label to y-axis
ax.set_ylabel("Values")

ax.legend(loc="upper right")

# And save the plot into raster format and vector format as well
fig.savefig("sensors.png")
fig.savefig("sensors.svg")

plt.show()
