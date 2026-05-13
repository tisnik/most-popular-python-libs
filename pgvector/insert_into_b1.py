#!/usr/bin/python
# vim: set fileencoding=utf-8

#
#  (C) Copyright 2025  Pavel Tisnovsky
#
#  All rights reserved. This program and the accompanying materials
#  are made available under the terms of the Eclipse Public License v1.0
#  which accompanies this distribution, and is available at
#  http://www.eclipse.org/legal/epl-v10.html
#
#  Contributors:
#      Pavel Tisnovsky
#

import psycopg2

import numpy as np
from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="localhost", port=54321, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

vectors = [
        "0000",
        "1111",
        "1100",
        "0011",
        ]

with connection.cursor() as cursor:
    for vector in vectors:
        cursor.execute("INSERT INTO b1 (embedding) VALUES (%s)", (vector, ))
    connection.commit()

