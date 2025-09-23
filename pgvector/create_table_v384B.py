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

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

print(connection)

CREATE_TABLE_STATEMENT = """
    CREATE TABLE IF NOT EXISTS v384b (
        id bigserial PRIMARY KEY,
        embedding vector(384) NOT NULL,
        sentence TEXT NOT NULL
    );
"""

LIST_TABLES_QUERY = """
    SELECT table_schema,table_name
      FROM information_schema.tables
     WHERE table_schema='public'
     ORDER BY table_schema,table_name;
"""

with connection.cursor() as cursor:
    print(CREATE_TABLE_STATEMENT)
    cursor.execute(CREATE_TABLE_STATEMENT)
    connection.commit()

    print(LIST_TABLES_QUERY)
    cursor.execute(LIST_TABLES_QUERY)
    tables = cursor.fetchall()

    for table in tables:
        print(table)
