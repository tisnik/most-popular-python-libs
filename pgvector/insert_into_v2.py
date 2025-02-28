import psycopg2

import numpy as np
from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

x = [-5, -4, -3,    3,  4,  5,   3, 3, 3, 4, 4, 4, 5, 5, 5]
y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5, 3, 4, 5, 3, 4, 5]

with connection.cursor() as cursor:
    for i in range(len(x)):
        vector = np.array([x[i], y[i]])
        print(vector)
        cursor.execute("INSERT INTO v2 (embedding) VALUES (%s)", (vector, ))
    connection.commit()

