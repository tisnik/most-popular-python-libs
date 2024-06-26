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


from minio import Minio

from pywebio import *
from pywebio.input import *
from pywebio.output import *

bucket_name = "sensors"
minio_address = "localhost:9000"
minio_access_key = "tester"
minio_secret_key = "tester01"

client = Minio(minio_address, minio_access_key, minio_secret_key, secure=False)


def main():
    put_info("Výsledky měření senzorů")
    found = client.bucket_exists(bucket_name)

    if not found:
        put_error("Data nelze přečíst - chybné připojení k Miniu")

    objects = client.list_objects(bucket_name, recursive=False)

    table = [["Senzor", "Datum", "Graf", "Info"]]

    for obj in objects:
        row = [obj.object_name, obj.last_modified, "Graf", "Data"]
        table.append(row)

    put_table(table)


start_server(main, port=8080, debug=True)
