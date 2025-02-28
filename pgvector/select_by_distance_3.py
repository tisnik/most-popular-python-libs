import psycopg2

from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

with connection.cursor() as cursor:
    query = """
        SELECT embedding
          FROM v2
         WHERE embedding <-> %s::vector < 2.5
    """
    cursor.execute(query, ([3,3], ))
    records = cursor.fetchall()
    for record in records:
        print(record[0])
