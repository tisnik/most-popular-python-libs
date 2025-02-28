import psycopg2

from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

with connection.cursor() as cursor:
    cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")
