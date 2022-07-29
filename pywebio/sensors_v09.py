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

from pywebio import *
from pywebio.input import *
from pywebio.output import *
from functools import partial

from io import StringIO
from minio import Minio, ResponseError

import pandas as pd


bucket_name = "sensors"
minio_address = "localhost:9000"
minio_access_key = "tester"
minio_secret_key = "tester01"

client = Minio(minio_address, minio_access_key, minio_secret_key, secure=False)


def show_data(bucket_name, sensor):
    response = client.get_object(bucket_name, sensor)
    buff = StringIO(response.read().decode())
    df = pd.read_csv(buff)

    popup(
        f"Data ze senzoru {sensor}",
        [
            put_text(f"Data ze senzoru {sensor}"),
            put_html(df.to_html(border=0)),
        ],
    )


def show_graph(sensor):
    popup(
        f"Graf pro senzor {sensor}",
        [
            put_text(f"Graf pro senzor {sensor}"),
        ],
    )


def main():
    put_info("Výsledky měření senzorů")
    found = client.bucket_exists(bucket_name)

    if not found:
        put_error("Data nelze přečíst - chybné připojení k Miniu")

    objects = client.list_objects(bucket_name, recursive=False)

    table = [["Senzor", "Datum", "Graf", "Info"]]

    for obj in objects:
        row = [
            obj.object_name,
            obj.last_modified,
            put_button("Graf", onclick=partial(show_graph, sensor=obj.object_name)),
            put_button(
                "Data",
                onclick=partial(
                    show_data, bucket_name=bucket_name, sensor=obj.object_name
                ),
            ),
        ]
        table.append(row)

    put_table(table)


start_server(main, port=8080, debug=True)
