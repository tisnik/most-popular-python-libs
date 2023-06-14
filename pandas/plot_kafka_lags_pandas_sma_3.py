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
    print("  plot_kafka_lags_pandas_sma_3.py input_file.csv")
    print("Example:")
    print("  plot_kafka_lags_pandas_sma_3.py overall.csv")
    sys.exit(1)

# First command line argument should contain name of input CSV.
input_csv = sys.argv[1]

df = pd.read_csv(input_csv)

for i in range(0, df.shape[0] - 2):
    df.loc[df.index[i + 2], "SMA_3"] = np.round(
        ((df.iloc[i, 1] + df.iloc[i + 1, 1] + df.iloc[i + 2, 1]) / 3), 1
    )

print(df)
print(df.info())
print(df.describe())

# Create new histogram graph
df.plot(x="Time", y=["topic : uploads", "SMA_3"])

# Try to show the plot on screen
plt.show()
