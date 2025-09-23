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

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

print(model)

sentences = [
    "The rain in Spain falls mainly on the plain",
    "The tesselated polygon is a special type of polygon",
    "The quick brown fox jumps over the lazy dog",
    "To be or not to be, that is the question",
    "It is a truth universally acknowledged...",
    "How old are you?",
    "The goat ran down the hill"
]

embeddings = model.encode(sentences)
print(f"Embeddings shape: {embeddings.shape}")

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

for sentence, vector in zip(sentences, embeddings):
    print(type(vector), vector.shape)
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO v384b (embedding, sentence) VALUES (%s, %s)", (vector, sentence))

connection.commit()
