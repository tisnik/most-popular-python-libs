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
import matplotlib.pyplot as plt

# Check if command line argument is specified (it is mandatory).
if len(sys.argv) < 2:
    print("Usage:")
    print("  plot_kafka_lags_pandas_2.py input_file.csv")
    print("Example:")
    print("  plot_kafka_lags_pandas_2.py overall.csv")
    sys.exit(1)

# First command line argument should contain name of input CSV.
input_csv = sys.argv[1]

df = pd.read_csv(input_csv)

print(df.info())
print(df.describe())

# Create new histogram graph
df.plot(x="Time", y="topic : uploads")

# Try to show the plot on screen
plt.show()
