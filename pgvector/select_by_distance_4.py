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
