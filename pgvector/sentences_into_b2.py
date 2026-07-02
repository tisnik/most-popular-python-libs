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
from sentence_transformers import SentenceTransformer

from pgvector.psycopg2 import register_vector

model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")

connection = psycopg2.connect(
    host="localhost", port=54321, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

CREATE_TABLE_STATEMENT = """
    CREATE TABLE IF NOT EXISTS b2 (
        id bigserial PRIMARY KEY,
        sentence TEXT NOT NULL,
        embedding bit (1024) NOT NULL
    );
"""

LIST_TABLES_QUERY = """
    SELECT table_schema,table_name
      FROM information_schema.tables
     WHERE table_schema='public'
     ORDER BY table_schema,table_name;
"""

with connection.cursor() as cursor:
    cursor.execute(CREATE_TABLE_STATEMENT)
    connection.commit()

    cursor.execute(LIST_TABLES_QUERY)
    tables = cursor.fetchall()

    for table in tables:
        print(table)

sentences = [
    "The rain in Spain falls mainly on the plain",
    "The tesselated polygon is a special type of polygon",
    "The quick brown fox jumps over the lazy dog",
    "To be or not to be, that is the question",
    "It is a truth universally acknowledged...",
    "How old are you?",
    "The goat ran down the hill"
]

embeddings = model.encode(sentences, precision="ubinary")
print(f"Embeddings shape: {embeddings.shape}")

for sentence, vector in zip(sentences, embeddings):
    print(type(vector), vector.shape)
    ascii_vector = ""
    for i, byte in enumerate(vector):
        ascii_vector += format(byte, "08b")
    print(ascii_vector)
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO b2 (sentence, embedding) VALUES (%s, %s)", (sentence, ascii_vector))

connection.commit()
