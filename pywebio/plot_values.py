#!/usr/bin/env python3

import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_values.py input_file.csv")
    print("Example:")
    print("  plot_values.py overall.csv")
    sys.exit(1)

# First command line argument should contain name of input CSV.
input_csv = sys.argv[1]

# Try to open the CSV file specified.
with open(input_csv) as csv_input:
    # And open this file as CSV
    csv_reader = csv.reader(csv_input)

    # Skip header
    next(csv_reader, None)
    rows = 0

    # Read all rows from the provided CSV file
    data = [(row[0], int(row[1])) for row in csv_reader]
    print(data)

# Linear regression
time = [item[0] for item in data]
messages = [item[1] for item in data]

# Linear regression
x = np.arange(0, len(messages))
coef = np.polyfit(x, messages, 1)
poly1d_fn = np.poly1d(coef)

# Create new histogram graph
plt.plot(messages, "b", poly1d_fn(np.arange(0, len(messages))), "y--")

# Title of a graph
plt.title("Sensor values")

# Add a label to x-axis
plt.xlabel("Time")

# Add a label to y-axis
plt.ylabel("Values")

plt.legend(loc="upper right")

# Set the plot layout
plt.tight_layout()

# And save the plot into raster format and vector format as well
plt.savefig("graph.png")
plt.savefig("graph.svg")

# Try to show the plot on screen
plt.show()
