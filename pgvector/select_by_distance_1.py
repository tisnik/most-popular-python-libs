import psycopg2

from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

with connection.cursor() as cursor:
    cursor.execute("SELECT embedding FROM v2 ORDER BY embedding <-> %s::vector LIMIT 5", ([3,3], ))
    records = cursor.fetchall()
    for record in records:
        print(record[0])
