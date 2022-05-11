#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from pywebio import *
from pywebio.input import *
from pywebio.output import *
from functools import partial

from io import StringIO
from minio import Minio, ResponseError

import io
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('agg')  # required, use a non-interactive backend

bucket_name = "sensors"
minio_address = "localhost:9000"
minio_access_key = "tester"
minio_secret_key = "tester01"

client = Minio(
    minio_address,
    minio_access_key,
    minio_secret_key,
    secure=False
)


def read_data_frame(bucket_name, sensor):
    response = client.get_object(bucket_name, sensor)
    buff = StringIO(response.read().decode())
    return pd.read_csv(buff)


def show_data(bucket_name, sensor):
    name = sensor[0:-4]

    df = read_data_frame(bucket_name, sensor)

    popup(f"Data ze senzoru {name}", [
        put_text(f"Data ze senzoru {name}"),
        put_html(df.to_html(border=0)),
    ])


def show_graph(bucket_name, sensor):
    name = sensor[0:-4]

    df = read_data_frame(bucket_name, sensor)

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

    # Save into buffer, not into file
    buf = io.BytesIO()
    fig.savefig(buf)
    fig.clear()
    plt.close(fig)

    popup(f"Graf pro senzor {name}", [
        put_text(f"Graf pro senzor {name}"),
        put_image(buf.getvalue())
    ])


def main():
    put_info("Výsledky měření senzorů")
    found = client.bucket_exists(bucket_name)

    if not found:
        put_error("Data nelze přečíst - chybné připojení k Miniu")

    objects = client.list_objects(bucket_name, recursive=False)

    table = [['Senzor', 'Datum', 'Graf', 'Info']]

    for obj in objects:
        row = [obj.object_name,
               obj.last_modified,
               put_button("Graf", onclick=partial(show_graph, bucket_name=bucket_name, sensor=obj.object_name)),
               put_button("Data", onclick=partial(show_data, bucket_name=bucket_name, sensor=obj.object_name))]
        table.append(row)

    put_table(table)


start_server(main, port=8080, debug=True)
