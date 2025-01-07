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

from io import StringIO

from minio import Minio, ResponseError

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

matplotlib.use("agg")  # required, use a non-interactive backend

bucket_name = "sensors"
minio_address = "localhost:9000"
minio_access_key = "tester"
minio_secret_key = "tester01"


def create_graph(filename, df):
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
    fig.savefig(filename)


def main():
    client = Minio(minio_address, minio_access_key, minio_secret_key, secure=False)

    found = client.bucket_exists(bucket_name)
    print("Bucket found:", found)

    objects = client.list_objects(bucket_name, recursive=False)

    for obj in objects:
        print(
            obj.bucket_name,
            obj.object_name,
            obj.last_modified,
            obj.etag,
            obj.size,
            obj.content_type,
        )
        try:
            response = client.get_object(bucket_name, obj.object_name)
            buff = StringIO(response.read().decode())
            df = pd.read_csv(buff)
            filename = obj.object_name[0:-4] + ".png"
            create_graph(filename, df)
        except ResponseError as err:
            print(err)
        finally:
            response.close()
            response.release_conn()


if __name__ == "__main__":
    main()
