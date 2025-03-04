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

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM v2")
    records = cursor.fetchall()
    for record in records:
        print(record)
