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

from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

query = """
    SELECT embedding
      FROM v2
     WHERE embedding <-> %s::vector < %s
"""

for distance in range(0, 10):
    with connection.cursor() as cursor:
        cursor.execute(query, ([3,3], distance))
        records = cursor.fetchall()
        for record in records:
            print(record[0])
    print("-"*50)
